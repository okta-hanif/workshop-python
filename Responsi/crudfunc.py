import sqlite3

conn = sqlite3.connect('responsi.db')
c = conn.cursor()
# c.execute(""" CREATE TABLE mahasiswa (
#    nim text,
#    nama text,
#    prodi text,
#    ipk real
# ) """)


#FUNCTIONS

def hapus_data(nim):
    # menghapus data
    c.execute("DELETE FROM mahasiswa WHERE nim = :nim",{'nim': nim})
    conn.commit()

def perbarui_data(nim, nama, prodi, ipk):
    # mengubah data
    c.execute('UPDATE mahasiswa SET nama = :nama, prodi = :prodi , ipk = :ipk WHERE nim = :nim',{
        'nim': nim, 'nama': nama, 'prodi':prodi, 'ipk':ipk })
    conn.commit()

def masukkan_data(nim, nama, prodi, ipk):
    # insert data
    c.execute("INSERT INTO mahasiswa VALUES(:nim,:nama,:prodi,:ipk)",{'nim': nim, 'nama': nama, 'prodi': prodi, 'ipk' : ipk})
    conn.commit()

def baca_data(nim):
    #perintah sql menampilkan data pada table
    c.execute('SELECT * FROM mahasiswa WHERE nim = :nim',{'nim': nim})
    conn.commit()

    # tampilan Data
    for row in c:
        print ("NIM     = ", row[0])
        print ("Nama    = ", row[1])
        print ("Prodi   = ", row[2])
        print ("IPK     = ", row[3])
        print ('')
