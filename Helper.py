#
#
#
# Reusable functions
#
#
#

import sympy
import math, cmath

def PiN(n):
    # The number of primes less than n.
    return len(list(sympy.sieve.primerange(0, n)))

def NoverPiN(n):
    return n / PiN(n)

def Basel(exp, terms):
    # 1 + 1 / 2^n + 1 / 3^n + 1 / 4^n + ...
    val = 0
    for n in range (1, terms + 1):
        val = val + (1 / n ** exp)
    return val

def Zeta(s, terms):
    # 1 + 1 / 2^s + 1 / 3^s + ... where s is a complex number.
    val = complex(0, 0)
    for n in range(1, terms + 1):
        val = val + (1 / n ** s)
    return val

def LogIntegral(x, terms):
    # https://math.stackexchange.com/questions/700391/integration-by-parts-of-the-logarithmic-integral
    # li(x) = Ei(lnx) = (γ + ln(lnx)) + [the cumulative sum from n=1 to infinity of: ((lnx)^n)/(n*n!)]
    y = 0.5772156649015328606065120
    val = y + math.log(math.log(x))
    for n in range(1, terms + 1):
        val = val + ((math.log(x))**n)/(n*(math.factorial(n)))
    if x > 2: val = val - 1.04516378011749278
    return val