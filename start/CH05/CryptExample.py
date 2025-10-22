#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Melinda 10/22

#install cryptography library
#pip3 install cryptography
from cryptography.fernet import Fernet 
# Create functions
# Fernate create key
def fernet_create_key():
    key = Fernet.generate_key()
    return key
# Fernate Encrypt
def fernet_encrypt(key, plain_text):
    key_b = key.encode()
    plain_text_b = plain_text.encode()
    cipher_text_b = Fernet( enc_key ).encrypt(plain_text_b )
    return cipher_text_b
# Fernet Decrypt 
def fernet_encrypt (key, cipher_text):
    key_b = key.encode()
    cipher_text_b = cipher_text.encode()
    plain_text_b = Fernet (key_b).decrypt(cipher_text_b)
    return plain_text_b

#Ask what to do
print ("*"*40)
print("Welcome to Fernat encryption")
print("This script can create keys, encrypt, or decrypt")
task = input ("what would you like to do (c/e/d)?")[0].lower()

#If encrput
if task == "e":
    #Get key and data
    enc_key=input("What is the key: ")
    plain_text = input ("What is the message: ")
    #Call encrypt function
    cipher_text_b = fernet_encrypt (enc_key, plain_text)
    # Print out results
    print ("Your encrupted message is")
    print (f"'{cipher_text_b.decode()}'")
#If decrypt
elif task == "d":
    #Get key and data
    enc_key = input ("What is the key: ")
    cipher_text = input ("What is the encrypted message: ")
    #Call decrypt function
    cipher_text_b = fernet_decrypt(enc_key, cipher_text)
    # Print out results
    print ("Your decrypted message is")
    print (f"'{plain_text_b.decode()}'")
#If create key
elif task == "c":
    #Call crete function
    enc_key_b = fernet_create_key()
    #Print out results
    enc_key = enc_key_b.decode()
    print (f"Encryption key '{enc_key}'")
else:
    print ("Please answer c/e/d")
