#!/usr/bin/env python
# -*- coding: utf-8 -*-
# imports
import random
import fractions
from primeGen import isPrime
from primeGen import generateRandomPrime
#imports#

# variables
#variables#

# classes
# classes

# math functions


def extendedGcd(a, b):
    # Returns pair (x, y) such that xa + yb = gcd(a, b)
    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty


def multiplicativeInverse(e, n):
    # Find the multiplicative inverse of e mod n.
    x, y = extendedGcd(e, n)
    if x < 0:
        return n + x
    return x
#math functions#

# RSA functions


def generateKeyManual(p, q):
    if p == q:
        print("Valores não válidos, devem ser diferentes.")
    elif p*q <= 256:
        print("Valores não válidos, p*q deve ser maior que 256.")
    elif(not isPrime(p) or not isPrime(q)):
        print("Valores não válidos, p e q devem ser primos.")
    else:
        n = p*q
        phi = (p-1)*(q-1)
        while True:
            e = random.randint(3, phi-1)
            if fractions.gcd(e, phi) == 1:
                break
        d = multiplicativeInverse(e, phi)
        return (n, e, d)


def generateKey(bits):
    p = generateRandomPrime(int(bits / 2))
    q = generateRandomPrime(int(bits / 2))
    # Ensure q != p, though for large values of bits this is
    # statistically very unlikely
    while q == p and q*p < 256:
        q = generateRandomPrime(int(bits / 2))
    n = p * q
    phi = (p - 1) * (q - 1)
    # Here we pick a random e, but a fixed value for e can also be used.
    while True:
        e = random.randint(3, phi - 1)
        if fractions.gcd(e, phi) == 1:
            break
    # encrypt((e,n),text)
    # decrypt((p,q,e),text)
    privateKey = multiplicativeInverse(e, phi)
    publicKey = e
    return (publicKey, privateKey, n)

# d


def encrypt(publicKey, n, plaintext):
    # Unpack the key into its components
    n = int(n)
    key = int(publicKey)
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m with fast modular exponentiation
    cipher = [str(pow(ord(char), key, n)) for char in plaintext]
    # Return the array of bytes
    return ' '.join(cipher)


def decrypt(privateKey, n, ciphertext):
    # Unpack the key into its components
    ciphertext = ciphertext.split()
    n = int(n)
    key = int(privateKey)
    # Generate the plaintext based on the ciphertext and key using a^b mod m with fast modular exponentiation
    plain = [chr(pow(int(char), key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)
#RSA functions#
