# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:58:49 2016

@author: JonEivind
"""
from __future__ import division

import numpy as np


# Diverse for RSA
# Først skal primtall p og q velges, så vi trenger metoder for å finne store primtall.
# generate_primes(start,stop) lister primtallene mellom start og stopp.
# Deretter er n = pq. check_key sjekker om en foreslått e er et lovlig valg.
# For en lovlig e regnes d ut ved å kalle mult_inverse((p-1)(q-1), e)
# Endelig er RSA_encrypt metoden for kryptering og dekryptering.

# eratosthenes genererer alle primtall < n
# Hvis n er et primtall er det ikke med.
def eratosthenes(n):
    rot = int(np.floor(np.sqrt(n)))
    alle_tall = list(range(n))
    alle_tall[1] = 0
    for i in range(rot + 1):
        if alle_tall[i] != 0:
            j = i
            while i * j < n:
                alle_tall[i * j] = 0
                j = j + 1
    return [tall for tall in alle_tall if tall != 0]


# generate_primes gir listen av primtall p med
# start <= p < stop
def generate_primes(start, stop):
    rot = int(np.floor(np.sqrt(stop)))
    primtall = eratosthenes(rot)
    alle_tall = list(range(start, stop))
    for tall in primtall:
        for i, rr in enumerate(alle_tall):
            if rr % tall == 0:
                alle_tall[i] = 0
    return [tall for tall in alle_tall if tall != 0]


# Velg to primtall fra en liste generert over, og kall dem p og q. Bruk n = pq.
# Forsøk med e til du finner en som har gcd(e,(p-1)(q-1))=1

def check_key(p, q, e):
    return gcd((p - 1) * (q - 1), e) == 1


# gcd er Euklids algoritme for å regne ut største felles divisor
def gcd(a, b):
    r = []
    q = []
    if a % b == 0:
        return b
    else:
        while a % b != 0:
            r.append(a % b)
            q.append((a - r[-1]) / b)
            a = b
            b = r[-1]
    return r[-1]


# regn ut d ved å kalle mult_inverse((p-1)(q-1), e)
def mult_inverse(a, b):
    original_a = a
    r = []
    q = []
    if gcd(a, b) != 1:
        return -1
    else:
        while a % b != 0:
            r.append(a % b)
            q.append(int((a - r[-1]) / b))
            a = b
            b = r[-1]
        y = [1]
        x = [-q[-1]]
        for j in range(1, len(q)):
            del q[-1]
            y.append(x[-1])
            x.append(y[-2] - q[-1] * x[-1])
        return x[-1] % original_a


# krypter med (n,e,klar), dekrypter med (n,d, kryptert)
def RSA_encrypt(n, e, klar):
    encrypted_list = []
    for single_word in klar:
        encrypted_list.append(powermod(single_word, e, n))
    return encrypted_list


# powermod(N,e,m) returns M = N^e mod m
def powermod(N, e, m):
    binary = bin(e)[2:]
    powers = [N % m]
    for n in range(1, len(binary)):
        powers.append(powers[-1] * powers[-1] % m)
    M = 1
    powerindex = 0
    for bit in reversed(binary):
        if bit == '1':
            M = M * powers[powerindex] % m
        powerindex = powerindex + 1
    return M
