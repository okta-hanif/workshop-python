#PRAKTIK 1

#!/usr/bin/env python3
"""
Test psycopg with CockroachDB.
"""

import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
from psycopg2.errors import SerializationFailure


def create_accounts(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS accounts (id INT PRIMARY KEY, balance INT)"
        )
        cur.execute("UPSERT INTO accounts (id, balance) VALUES (1, 1000), (2, 250)")
        logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()


def delete_accounts(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM bank.accounts")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()


def print_balances(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, balance FROM accounts")
        logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        print(f"Balances at {time.asctime()}:")
        for row in rows:
            print(row)


def transfer_funds(conn, frm, to, amount):
    with conn.cursor() as cur:

        # Check the current balance.
        cur.execute("SELECT balance FROM accounts WHERE id = %s", (frm,))
        from_balance = cur.fetchone()[0]
        if from_balance < amount:
            raise RuntimeError(
                f"Insufficient funds in {frm}: have {from_balance}, need {amount}"
            )

        # Perform the transfer.
        cur.execute(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, frm)
        )
        cur.execute(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, to)
        )

    conn.commit()
    logging.debug("transfer_funds(): status message: %s", cur.statusmessage)


def run_transaction(conn, op, max_retries=3):
    """
    Execute the operation *op(conn)* retrying serialization failure.

    If the database returns an error asking to retry the transaction, retry it
    *max_retries* times before giving up (and propagate it).
    """
    # leaving this block the transaction will commit or rollback
    # (if leaving with an exception)
    with conn:
        for retry in range(1, max_retries + 1):
            try:
                op(conn)

                # If we reach this point, we were able to commit, so we break
                # from the retry loop.
                return

            except SerializationFailure as e:
                # This is a retry error, so we roll back the current
                # transaction and sleep for a bit before retrying. The
                # sleep time increases for each failed transaction.
                logging.debug("got error: %s", e)
                conn.rollback()
                logging.debug("EXECUTE SERIALIZATION_FAILURE BRANCH")
                sleep_ms = (2 ** retry) * 0.1 * (random.random() + 0.5)
                logging.debug("Sleeping %s seconds", sleep_ms)
                time.sleep(sleep_ms)

            except psycopg2.Error as e:
                logging.debug("got error: %s", e)
                logging.debug("EXECUTE NON-SERIALIZATION_FAILURE BRANCH")
                raise e

        raise ValueError(f"Transaction did not succeed after {max_retries} retries")


def test_retry_loop(conn):
    """
    Cause a seralization error in the connection.

    This function can be used to test retry logic.
    """
    with conn.cursor() as cur:
        # The first statement in a transaction can be retried transparently on
        # the server, so we need to add a dummy statement so that our
        # force_retry() statement isn't the first one.
        cur.execute("SELECT now()")
        cur.execute("SELECT crdb_internal.force_retry('1s'::INTERVAL)")
    logging.debug("test_retry_loop(): status message: %s", cur.statusmessage)


def main():
    opt = parse_cmdline()
    logging.basicConfig(level=logging.DEBUG if opt.verbose else logging.INFO)

    conn = psycopg2.connect(opt.dsn)
    create_accounts(conn)
    print_balances(conn)

    amount = 100
    fromId = 1
    toId = 2

    try:
        run_transaction(conn, lambda conn: transfer_funds(conn, fromId, toId, amount))

        # The function below is used to test the transaction retry logic.  It
        # can be deleted from production code.
        # run_transaction(conn, test_retry_loop)
    except ValueError as ve:
        # Below, we print the error and continue on so this example is easy to
        # run (and run, and run...).  In real code you should handle this error
        # and any others thrown by the database interaction.
        logging.debug("run_transaction(conn, op) failed: %s", ve)
        pass

    print_balances(conn)

    delete_accounts(conn)

    # Close communication with the database.
    conn.close()


def parse_cmdline():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "dsn",
        help="database connection string\n\n"
             "For cockroach demo, use postgresql://<username>:<password>@<hostname>:<port>/bank?sslmode=require,\n"
             "with the username and password created in the demo cluster, and the hostname and port listed in the\n"
             "(sql/tcp) connection parameters of the demo cluster welcome message."
    )

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="print debug info")

    opt = parser.parse_args()
    return opt


if __name__ == "__main__":
    main()



###PRAKTIK 2
"""This module performs the following steps sequentially:
    1. Reads in existing account IDs (if any) from the bank database.
    2. Creates additional accounts with randomly generated IDs. Then, it adds a bit of money to each new account.
    3. Chooses two accounts at random and takes half of the money from the first and deposits it into the second.
"""

import random
from math import floor
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cockroachdb.sqlalchemy import run_transaction

Base = declarative_base()



class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Integer)


# Create an engine to communicate with the database. The
# "cockroachdb://" prefix for the engine URL indicates that we are
# connecting to CockroachDB using the 'cockroachdb' dialect.
# For more information, see
# https://github.com/cockroachdb/sqlalchemy-cockroachdb.

engine = create_engine(
    # For cockroach demo:
    'cockroachdb://<username>:<password>@<hostname>:<port>/bank?sslmode=require',
    echo=True                   # Log SQL queries to stdout
)

# Automatically create the "accounts" table based on the Account class.
Base.metadata.create_all(engine)


# Store the account IDs we create for later use.

seen_account_ids = set()


# The code below generates random IDs for new accounts.

def create_random_accounts(sess, num):
    """Create N new accounts with random IDs and random account balances.
    Note that since this is a demo, we don't do any work to ensure the
    new IDs don't collide with existing IDs.
    """
    new_accounts = []
    while num > 0:
        billion = 1000000000
        new_id = floor(random.random()*billion)
        seen_account_ids.add(new_id)
        new_accounts.append(
            Account(
                id=new_id,
                balance=floor(random.random()*1000000)
            )
        )
        num = num - 1
    sess.add_all(new_accounts)


run_transaction(sessionmaker(bind=engine),
                lambda s: create_random_accounts(s, 100))


def get_random_account_id():
    """ Helper function for getting random existing account IDs.
    """
    random_id = random.choice(tuple(seen_account_ids))
    return random_id


def transfer_funds_randomly(session):
    """Transfer money randomly between accounts (during SESSION).
    Cuts a randomly selected account's balance in half, and gives the
    other half to some other randomly selected account.
    """
    source_id = get_random_account_id()
    sink_id = get_random_account_id()

    source = session.query(Account).filter_by(id=source_id).one()
    amount = floor(source.balance/2)

    # Check balance of the first account.
    if source.balance < amount:
        raise "Insufficient funds"

    source.balance -= amount
    session.query(Account).filter_by(id=sink_id).update(
        {"balance": (Account.balance + amount)}
    )


# Run the transfer inside a transaction.

run_transaction(sessionmaker(bind=engine), transfer_funds_randomly)