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
# trabalho functions
def asciiToAmorim(char):
	if(char == " "):
		 return 26
	elif(ord(char.upper())>=65 and ord(char.upper()) < 65+26):
		return ord(char.upper())-65
	else:
		return 26

def amorimToAscii(numb):
	if(numb == 26):
		return " "
	else:
		return chr(numb+65)
# trabalho functions
# RSA functions

def generatePrivateKey(p,q):
	phi = (p-1)*(q-1)
	while True:
		e = random.randint(3, phi-1)
		if fractions.gcd(e,phi) == 1:
			break
	return e
		
def generatePublicKey(p, q, e):
	if p == q:
		print("Valores não válidos, devem ser diferentes.")
	elif p*q <= 256:
		print("Valores não válidos, p*q deve ser maior que 256.")
	elif(not isPrime(p) or not isPrime(q)):
		print("Valores não válidos, p e q devem ser primos.")
	elif(fractions.gcd(e,((p-1)*(q-1)))!=1):
		print("Valores não válidos, 'e' deve ser coprimo a (p-1)*(q-1)")
	else:
		n = p*q
		phi = (p-1)*(q-1)
		d = multiplicativeInverse(e, phi)
		return (n, e, d)

def encrypt(publicKey, n, plaintext):
    # Unpack the key into its components
    n = int(n)
    key = int(publicKey)
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m with fast modular exponentiation
    cipher = [pow(asciiToAmorim(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(privateKey, n, ciphertext):
	# Unpack the key into its components
	#ciphertext = ciphertext.split()
	n = int(n)
	key = int(privateKey)
	# Generate the plaintext based on the ciphertext and key using a^b mod m with fast modular exponentiation
	plain = [pow(int(char), key, n) for char in ciphertext]
	plain = [amorimToAscii(char) for char in plain]
	# Return the array of bytes as a string
	return ''.join(plain)
#RSA functions#
