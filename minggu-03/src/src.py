fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4) ) # Find next banana starting a position 4
print(fruits.reverse())
print(fruits.append('grape'))
print(fruits.sort())
print(fruits.pop())

stack = [3, 4, 5]
print(stack.append(6))
print(stack.append(7))
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue.append("Terry"))          # Terry arrives
print(queue.append("Graham"))          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)                           # Remaining queue in order of arrivalf

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print()

print(squares = list(map(lambda x: x**2, range(10))))
print(squares = [x**2 for x in range(10)])

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

combs = []
 for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))

print(combs) 

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
#[x, x**2 for x in range(6)]  ERROR

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
print()
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

print(list(zip(*matrix)))


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
#print(a) ERROR karna sudah dihapus

t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable:
    #t[0] = 88888 ERROR 
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
print()

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton) 

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
print('orange' in basket)                 # fast membership testing
print('crabgrass' in basket)
   # Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                              # unique letters in a
print(a - b)                            # letters in a but not in b
print(a | b)                             # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print()

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print()

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print()

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

print()

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)