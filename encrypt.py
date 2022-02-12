#!/usr/bin/env python
# coding: utf-8

# Braden Kattman and Trey Kline
# CSSE 473 - RSA Implementation
# Encrypting a Message Given 
# February 11, 2022

# Import Statements
import sys

# Parsing script arguments
nLoc = "./bin/n.txt"
eLoc = "./bin/e.txt"
for i in range(1, len(sys.argv), 2):
    if sys.argv[i] in ['-n', '--key-loc']:
        nLoc = sys.argv[i+1]
    elif sys.argv[i] in ['-e', '--exp-loc']:
        eLoc = sys.argv[i+1]
    elif sys.argv[i] in ['-m', '--message']:
        message = sys.argv[i+1]
    elif sys.argv[i] in ['-l', '--message-loc']:
        messageLoc = sys.argv[i+1]
        messageFile = open(messageLoc, "r")
        message = messageFile.read()
        messageFile.close()

# Loading the public keys from the
#  supplied file locations
nFile = open(nLoc, "r")
eFile = open(eLoc, "r")
n = int(nFile.read())
e = int(eFile.read())
nFile.close()
eFile.close()

# Encoding Algorithm
# Converts our message string into a
#  base-128 integer mapped character-
#  by-character according to its ASCII
#  value, and converts that to a standard
#  base-10 integer to be calculated on
#  for encrypting.
encoded = 0
for i in range(len(message)):
    encoded += int(pow(128, i) * ord(message[i]))

# Encrypting Algorithm
# Sets our encrypted message value
#  to be (encoded ^ e) % n
encrypted = pow(encoded, e, n)

# Writing our encoded message to the
#  file encoded.txt in ./bin
encodedFile = open("./bin/encoded.txt", "w")
encodedFile.write(str(encoded))
encodedFile.close()

# Writing our fully encrypted message
#  to the file encoded.txt in ./bin
encryptedFile = open("./bin/encrypted.txt", "w")
encryptedFile.write(str(encrypted))
encryptedFile.close()
