
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

import fibo

fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

fib = fibo.fib
fib(500)


from fibo import fib, fib2
fib(500)

from fibo import *
fib(500)

import  sys
print(dir(fibo))
print()
print(dir(sys))


a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print(dir())
print()


import builtins
print(dir(builtins))

import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)

