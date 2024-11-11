# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:52:53 2024

@author: xMiku
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generer_clefs():
    clef = RSA.generate(2048)
    clef_privee = clef
    clef_publique = clef.publickey()
    return clef_privee, clef_publique

def chiffrer_message(message, clef_publique):
    chiffreur = PKCS1_OAEP.new(clef_publique)
    message_chiffre = chiffreur.encrypt(message.encode('utf-8'))
    return message_chiffre

def dechiffrer_message(message_chiffre, clef_privee):
    chiffreur = PKCS1_OAEP.new(clef_privee)
    message_dechiffre = chiffreur.decrypt(message_chiffre)
    return message_dechiffre.decode('utf-8')

clef_privee, clef_publique = generer_clefs()
message = "Bonjour, ceci est un message secret!"
message_chiffre = chiffrer_message(message, clef_publique)
message_dechiffre = dechiffrer_message(message_chiffre, clef_privee)

print("Clé publique:", clef_publique.export_key().decode())
print("Clé privée:", clef_privee.export_key().decode())
print("\nMessage original:", message)
print("\nMessage chiffré:", message_chiffre)
print("\nMessage déchiffré:", message_dechiffre)