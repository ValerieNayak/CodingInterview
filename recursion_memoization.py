# Valerie Nayak
# 3/23/2020
# Socratica: https://www.youtube.com/watch?v=Qk0zUZW-U_M
# Recursion and Memoization

from functools import lru_cache

def fibonacci(n):
    # fibonacci recursive function without memoization
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# print the first n numbers of sequence (this gets increasingly slow)
# for n in range(1, 11):
#     print(n, ":", fibonacci(n))

##### NOW WITH MEMOIZATION
# idea: cache values of previous recursive function calls

fibonacci_cache = {}
def fib_mem(n):
    # fibonacci recursive with memoization
    # if we have the cached value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fib_mem(n-1) + fib_mem(n-2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value

# print first 100 values - works much faster!
# for n in range(1, 101):
#     print(n, ":", fib_mem(n))

#### MEMOIZATION WITH PYTHON LIBRARY
# This will allow you to implement memoization in a single line

@lru_cache(maxsize = 1000)
def fib_mem_short(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib_mem_short(n-1) + fib_mem_short(n-2)

# try it!
for n in range(1, 501):
    print(n, ":", fib_mem_short(n))
