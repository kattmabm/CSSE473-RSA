# RSA Algorithm

**Braden Kattman and Trey Kline**

## Overview

This project was created for Rose-Hulman's CSSE 473 - Design and Analysis of Algorithms class. We aimed to review the history of the creation of the RSA encryption algorithm, as well as implement our own version in Python.

## How to Run

This project contains three Python scripts that accomplish everything necessary to show the fully-functional RSA encryption algorithm.

``generateKeys.py`` generates the public and private keys used for encrypting and decrypting the data recieved.

``encrypt.py`` encodes and encrpyts a user's message given the public key.

``decrypt.py`` decrypts and decodes an encrypted message given the private key.

### Generate Keys

#### Arguments

 - ``--length`` (``-l``) : Approximate base-10 length of the prime numbers that should be used to generate the public and private keys. Default value: ``100``.

#### Outputs

Outputs the following files to the ``./private`` directory:

 - ``d.txt`` : Contains the private key value *d*.

 - ``p.txt`` : Contains our first randomly generated prime number.

 - ``q.txt`` : Contains our second randomly generated prime number.

Outputs the following files to the ``./public`` directory:

 - ``e.txt`` : Contains the public key exponent value *e*.

 - ``n.txt`` : Contains the public key produuct value *n*.

### Encrypt

**Warning**: some errors may occur when attempting to encrypt messages that are more than 100 characters long or so. I believe this has to do with Python's ``pow()`` method becoming somewhat probabilistic when working with truly massive numbers, but more testing is needed to figure out the exact cause.

#### Arguments

 - ``--key-loc`` (``-n``) : File location containing the product portion of the public key, *n*. Default value: ``./public/n.txt``.

 - ``--exp-loc`` (``-e``) : File location containing the exponent portion of the public key, *e*. Default value: ``./public/e.txt``.

 - ``--message-loc`` (``-m``) : File location containing the message that is to be encrypted. Default value: ``./message/message.txt``.

#### Outputs

Outputs the following files to the ``./public`` directory:

 - ``encrpyted.txt`` : The user-inputted message after being fully encoded and encrypted using RSA encryption.

### Decrypt

#### Arguments

 - ``--public-loc`` (``-n``) : File location containing the product portion of the public key, *n*. Default value: ``./public/n.txt``.

 - ``--private-loc`` (``-d``) : File location containing the private key, *d*. Default value: ``./private/d.txt``.

 - ``--message-loc`` (``-m``) : File location containing the encrypted message to be decrypted. Default value: ``./public/encrypted.txt``.

#### Outputs

Outputs the following files to the ``./private`` directory:

 - ``decoded.txt`` : The message that has been fully decoded using the RSA alorithm.
