#!/usr/bin/env python
# coding: utf-8

# Braden Kattman and Trey Kline
# CSSE 473 - RSA Implementation
# Generating Public and Private Keys
# February 11, 2022

# Import Statements
import sys
import os
from math import floor
from math import gcd
from math import log
from random import randint
from Crypto.Util import number

# Parsing script arguments
digits = 100
for i in range(1, len(sys.argv), 2):
    if sys.argv[i] in ['-l', '--length']:
        digits = int(sys.argv[i+1])

# Converting base-10 digits to
#  base-2 bit length
bitLength = floor(digits * log(10, 2))

# Generating two unique primes p and q
#  of the desired length (with some
#  random length variation added in)
p = 0
q = 0
while p == q:
    p = number.getPrime(bitLength + randint(-5, 5))
    q = number.getPrime(bitLength + randint(-5, 5))

# Calculating our public and private
#  key value n to be the product of
#  our two generated prime numbers
n = p * q

# Calculating phi to be the product
#  of p - 1 and q - 1
phi = (p-1) * (q-1)

# Finding our encryption public key
#  exponent e which is the smallest
#  value that is coprime with phi.
for e in range(2, phi):
    if gcd(e, phi) == 1:
        break

# Setting our private key d to be
#  the modular multiplicative inverse
#  of the product of e * phi.
d = pow(e, -1, phi)

# Creating the ./bin directory if
#  it does not already exist.
outputFolder = "./bin"
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Writing our private key d to the
#  file d.txt in ./bin
dFile = open("./bin/d.txt", "w")
dFile.write(str(d))
dFile.close()

# Writing our public key exponent
#  e to the file e.txt in ./bin
eFile = open("./bin/e.txt", "w")
eFile.write(str(e))
eFile.close()

# Writing our public key value n
#  to the file n.txt in ./bin
nFile = open("./bin/n.txt", "w")
nFile.write(str(n))
nFile.close()

# Writing our first prime number
#  p to the file p.txt in ./bin
pFile = open("./bin/p.txt", "w")
pFile.write(str(p))
pFile.close()

# Writing our second prime number
#  q to the file q.txt in ./bin
qFile = open("./bin/q.txt", "w")
qFile.write(str(q))
qFile.close()
