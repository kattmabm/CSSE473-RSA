# RSA Algorithm

**Braden Kattman and Trey Kline**

## Overview

This project was created for Rose-Hulman's CSSE 473 - Design and Analysis of Algorithms class. We aimed to review the history of the creation of the RSA encryption algorithm, as well as implement our own version in Python.

## How to Run

This project contains three Python scripts that accomplish everything necessary to show the fully-functional RSA encryption algorithm.
``generateKeys.py`` generates the public and private keys used for encrypting and decrypting the data recieved. ``encrypt.py`` encodes and encrpyts a user's message given the public key. ``decrypt.py`` decrypts and decodes an encrypted message given the private key.

### Generate Keys

#### Arguments

 - ``--length`` (``-l``) : Approximate base-10 length of the prime numbers that should be used to generate the public and private keys. Default value: ``100``.

#### Outputs

Outputs the following files to the ``./bin`` directory:

 - ``d.txt`` : Contains the private key value $d$.

 - ``e.txt`` : Contains the public key exponent value $e$.

 - ``n.txt`` : Contains the public key produuct value $n$.

 - ``p.txt`` : Contains our first randomly generated prime number.

 - ``q.txt`` : Contains our second randomly generated prime number.

### Encrypt

#### Arguments

 - ``--key-loc`` (``-n``) : File location containing the product portion of the public key, $n$. Default value: ``./bin/n.txt``.

 - ``--exp-loc`` (``-e``) : File location containing the exponent portion of the public key, $n$. Default value: ``./bin/e.txt``.

 - ``--message-loc`` (``-l``) : File location containing the message that is to be encrypted.

 - ``--message`` (``-m``) : Message to be encoded and encrpyted. This can be substituted for ``--message-loc`` if a message is typed directly rather than giving a file path.

#### Outputs

Outputs the following files to the ``./bin`` directory:

 - ``encoded.txt`` : An encoded copy of the user-inputted message. This is *not* the encrypted value, it has simply been converted from ASCII characters to an integer.

 - ``encrpyted.txt`` : The user-inputted message after being fully encoded and encrypted using RSA encryption.

### Decrypt

Not yet implemented.