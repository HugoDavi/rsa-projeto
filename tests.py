#imports
import rsa
import prime_gen as pg
from random import randint
from math import sqrt
#imports#

#classes
#classes#

#functions
def gcd(a,b):#Mathematically proven to work, so doesn't require its own test?
    if(b == 0):
        return(a)
    else:
        return gcd(b,a%b)

def testExtendedGcd():
    a,b = randint(0,1024),randint(0,1024)
    x,y = rsa.extendedGcd(a,b)
    greaterCommonDivisor = gcd(a,b)
    result = x*a+y*b
    assert(result==greaterCommonDivisor)

def testPrimeChecker():
    for i in range(500):
        val = randint(2,2048)
        a = pg.primeChecker(val)
        b = True
        for i in range(2,val):#Slow but certain prime checking method
            if(val%i==0):
                print(val,i)
                b = False
                break
        if a!=b:
            assert a==b,"inconclusive at %d"%val

def testEncryptDecrypt():
    for i in range(10):
        pubKey,privKey,modN = rsa.generateKey(randint(1,4096))
        cypher = ''
        for i in range(10):
            cypher+=chr(randint(65,90))
        assert(cypher== rsa.decrypt(privKey,modN,rsa.encrypt(pubKey,modN,cypher)))
#functions#

#variables
#variales#

#main
#main#

def main():
    return 0

if __name__ == "__main__":
    main()
