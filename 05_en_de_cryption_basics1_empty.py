# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
05_en_de_cryption_basics1.py

Šifrování - na vstupu bude string, výstupem zakódovaný text
* Caesarova šifra - zjistěte princip, napište jednoduchou variantu s posunem o 3 znaky, malá písmena ENG. Výstupem bude střing.
* Rozšiřte předchozí variantu o nastavitelný parametr - posun. Výstupem bude string.
** Udělejte variantu s Case sensitive a komplet CZ znakovou sadou, speciální znaky ponechte beze změny.
* Rozšiřte předchozí variantu o dešifrování zašifrovaných znaků.
"""

import os

alphabet_lower = []
for i in range(97, 123):
    alphabet_lower.append(chr(i))

alphabet = []
for i in list(range(65, 91)) + list(range(97, 123)):
    alphabet.append(chr(i))
##############################################################
### Caesar - základ - posun přesně o 3 znaky, pouze eng malé
# funkce caesar_cipher_basic

def caesar_cipher_basic(userinput, n = 3):
    output = ""
  
    for character in userinput:
        index1 =  alphabet_lower.index(character)
        output += alphabet_lower[(index1+n)%len(alphabet_lower)]

    return output
    
    




##############################################################
### Caesar - základ - posun o "shift" znaků, pouze eng malé
# funkce caesar_cipher_with_shift
def caesar_cipher_with_shift(userinput, input_text):
    output = ""
   
    for character in userinput:
        index1 =  alphabet_lower.index(character)
        output += alphabet_lower[(index1+input_text)%len(alphabet_lower)]
    

    return output





##############################################################
### Caesarova šifra s rozlišením malých a velkých písmen a české abecedy 
# funkce caesar_cipher_cz_with_diacritics
def caesar_cipher_cz_with_diacritics(userinput, input_text):
    output = ""
    czalphabet = "AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽaábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž"
    
    for character in userinput:
        index1 =  czalphabet.index(character)
        output += czalphabet[(index1+input_text)%len(czalphabet)]
    

    return output




##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    # Test s posunem přesně o 3 znaky
    print("Caesar - základ - posun o 3 znaky, pouze eng malé\n")
    input_text = input("Zadejte text pro zašifrování: ")
    print("Zašifrovaný text:", caesar_cipher_basic(input_text))
    print("------------------------------------------------\n")

    # Test s nastavitelným posunem
    print("Caesar - základ - posun o zadaný počet znaků, pouze eng malé\n")
    input_text = input("Zadejte text pro zašifrování: ")
    shift = int(input("Zadejte posun: "))
    print("Zašifrovaný text:", caesar_cipher_with_shift(input_text, shift))
    print("------------------------------------------------\n")

    # Test včetně celé české abecedy
    print("Caesarova šifra s podporou velkých písmen a české abecedy\n")
    input_text = input("Zadejte text pro zašifrování: ")
    shift = int(input("Zadejte posun: "))

    # Zašifrování
    encrypted_text = caesar_cipher_cz_with_diacritics(input_text, shift)
    print("Zašifrovaný text:", encrypted_text)

    # Dešifrování
    decrypted_text = caesar_cipher_cz_with_diacritics(encrypted_text, -shift)
    print("Dešifrovaný text:", decrypted_text)
    print("------------------------------------------------\n")