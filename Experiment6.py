#
#
#
# Primes less than n.
#
#
#

import sympy

def PrimesLessThanN(n):
    return len(list(sympy.sieve.primerange(0, n)))
        
print(PrimesLessThanN(1000))
print(PrimesLessThanN(1000000)) 