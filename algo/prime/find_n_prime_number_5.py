#!/usr/bin/python2.7
def primes():
    yield 2 ; yield 3 ; yield 5 ; yield 7 ;
    ps = (p for p in primes())              # additional primes supply
    p = ps.next() and ps.next()             # discard 2, then get 3
    q = p*p                                 # 9 - square of next prime to be put
    sieve = {}                              #       into sieve dict
    n = 9                                   # the candidate number
    while True:
        if n not in sieve:                  # is not a multiple of previously recorded primes
            if n < q:                       # n is prime
                yield n  
            else:
                add(sieve, q + 2*p, 2*p)    # n==p*p: for prime p, under p*p + 2*p, 
                p = ps.next()               #         add 2*p as incremental step
                q = p*p
        else:
            s = sieve.pop(n)
            add(sieve, n + s, s)
        n += 2                              # work on odds only
 
def add(sieve,next,step):
    while next in sieve:                    # ensure each entry is unique
        next += step
    sieve[next] = step                      # next non-marked multiple of a prime
 
import itertools
def primes_up_to(limit):
    return list(itertools.takewhile(lambda p: p <= limit, primes()))

# The above code is from http://rosettacode.org/wiki/Sieve_of_Eratosthenes#Python
# I have simply used the generator in a different way to get the nth prime number
# instead of a list of n primes. This is 'marginally' faster (about a 100ms for 
# giving the output to:
# %timeit get_nth_prime(100001)
# as compared to
# %timeit primes_up_to(1299721))

def get_nth_prime(n):
    return (pnum for index,pnum in enumerate(primes()) if index == n-1).next()

print(get_nth_prime(1000001))
