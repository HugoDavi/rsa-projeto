#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO
# imports
import rsa
import sys
from rsa import encrypt
from rsa import decrypt
from rsa import generatePrivateKey, generatePublicKey
# main


def gerar_chave():
    p = int(input("Escolha um valor para p: "))
    q = int(input("Escolha um valor para p: "))
    e = int(input("Escolhe um valor para e: "))
    (n, e, d) = generatePublicKey(p, q, e)
    with open("pub.txt", "w") as f:
        f.write("e = {}\n n = {}".format(e, n))
    with open("priv.txt","w") as f:
        f.write("d = {}\n n = {}".format(d,n))
    # privada = e, n (numero x elevado a e mód n)
    # publica = d, n (numero x elevado a d mód n)


def encriptografar():
    message = input("Digite mensagem para encriptar: ")
    e = int(input("Digite e: "))
    n = int(input("Digite n: "))

    encripted = encrypt(e, n, message)
    encripted = [str(x) for x in encripted]
    with open("cipher.txt") as f:
                f.write(" ".join(encripted))

def desencriptografar():
    p = input("Insira o p: ")
    q = input("Insira o q: ")
    e = input("Insira o e: ")
    encripted_text = input("Digite o texto encriptado(Separado): ")
    n,e,d = generatePublicKey(p,q,e)
    message = decrypt(d,n, encripted_text)
    with open("Decypher.txt","w") as f:
        f.write(message)


def main():
    should_run = True
    while(should_run):
        print("Escolha uma opção:\n1. gerar chaves \n2. encriptografar \n3. descriptografar\n4. encerrar")
        escolhe = int(input())

        if escolhe is 4:
            should_run = False
        elif escolhe is 1:
            gerar_chave()
        elif escolhe is 2:
            encriptografar()
        elif escolhe is 3:
            desencriptografar()
        else:
            continue


if __name__ == "__main__":
    main()
