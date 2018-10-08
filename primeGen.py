#imports
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import primesList
from math import sqrt
#imports#

#variables
#variables#

#classes
#classes#

#functions
def isPrime(value):
    primes = primesList.lessThanHundredThousand
    for prime in primes:
        if value == prime:
            return True
        elif value%prime==0:
            return False
        
    for prim in range(prime,int(sqrt(value)),2):
        if(value%prim==0):
            return False
    return True

def generateRandomPrime(intervalo):
    prime = 0
    while(not isPrime(prime)):
        prime = randint(0,intervalo)
    return prime

#functions#
