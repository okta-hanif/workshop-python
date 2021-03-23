year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

s = 'Hello, world.'
print(str(s))
print(repr(s) )
print(str(1/7) )
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))) )

print( )

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
print()

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
print()

#Basic usage of the str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#A number in the brackets can be used to refer to the position of the 
# object passed into the str.format() method.
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
#keyword arguments
print('This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))
#Positional and keyword arguments
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    'Dcab: {0[Dcab]:d}'.format(table))

#passing the table as keyword arguments with the ‘**’ notation.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#example
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print()

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

print()

#import math
print('The value of pi is approximately %5.3f.' % math.pi)

# f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()
print(read_data)

# We can check that the file has been automatically closed.
print(f.closed)

print()

import json
print(json.dumps([1, 'simple', 'list']))

