#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO
# imports
import rsa
import sys
from rsa import generateKeyManual
from rsa import encrypt
from rsa import decrypt
# main


def gerar_chave():
    p = int(input("Escolha um valor para p: "))
    q = int(input("Escolha um valor para p: "))
    (n, e, d) = generateKeyManual(p, q)
    print(n, e, d)
    # publica, privada, inverso mulriplicativo


def encriptografar():
    message = input("Ditite mensagem para encriptar: ")
    d = int(input("Digite d: "))
    n = int(input("Digite n: "))

    encripted = encrypt(d, n, message)
    print("PRINITING....................")
    print(encripted)


def desencriptografar():
    private_key = int(input("Digite a chave privada: "))
    public_key = int(input("Digite a chave publica: "))
    encripted_text = input("Digite o texto encriptado: ")
    message = decrypt(private_key, public_key, encripted_text)
    print(message)


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
