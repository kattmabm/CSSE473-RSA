#!/usr/bin/env python
# coding: utf-8

# Braden Kattman and Trey Kline
# CSSE 473 - RSA Implementation
# Encrypting a Message Given 
# February 11, 2022

# Import Statements
import sys
from math import log
from math import floor

# Parsing script arguments
nLoc = "./bin/n.txt"
dLoc = "./bin/d.txt"
messageLoc = "./bin/encrypted.txt"
for i in range(1, len(sys.argv), 2):
    if sys.argv[i] in ['-n', '--public-loc']:
        nLoc = sys.argv[i+1]
    elif sys.argv[i] in ['-d', '--private-loc']:
        eLoc = sys.argv[i+1]
    elif sys.argv[i] in ['-l', '--message-loc']:
        messageLoc = sys.argv[i+1]

messageFile = open(messageLoc, "r")
encrypted = int(messageFile.read())
messageFile.close()

# Loading the public keys from the
#  supplied file locations
nFile = open(nLoc, "r")
dFile = open(dLoc, "r")
n = int(nFile.read())
d = int(dFile.read())
nFile.close()
dFile.close()

# Decrypting Algorithm
# Sets our decrypted message value
#  to be (encrypted ^ d) % n
decrypted = pow(encrypted, d, n)

# Decoding Algorithm
# Converts our base-10 integer into a
#  base-128 integer, assigns each digit
#  to its corresponding ASCII value, and
#  reads this off as a string.
numToDecode = decrypted
decoded = ""
for i in range(floor(log(numToDecode, 128)), -1, -1):
    base = int(pow(128, i))
    letter = floor(numToDecode / base)
    decoded += chr(letter)
    numToDecode -= letter * base
decoded = decoded[::-1]

# Writing our decrypted message to the
#  file encoded.txt in ./bin
decryptedFile = open("./bin/decrypted.txt", "w")
decryptedFile.write(str(decrypted))
decryptedFile.close()

# Writing our fully decoded message
#  to the file encoded.txt in ./bin
decodedFile = open("./bin/decoded.txt", "w")
decodedFile.write(str(decoded))
decodedFile.close()
