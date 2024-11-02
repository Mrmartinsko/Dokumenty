# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""
05_en_de_cryption_basics2.py

Rozšířená Caesarova šifra
1. Různý posun pro každý znak v textu dle vzoru.
2. Posun na úrovni celých slov.
3. Hrubou silou dešifrovat zprávu, pokud známe abecedu.
"""

# Globální konstanty a proměnné
MY_ALPHABET = "aábcčdďeéěfghijklmnňoópqrřsštťuůúvwxyzž0123456789.,-+?!AÁBCČDĎEÉĚFGHIJKLMNŇOÓPQRŘSŠTŤUŮÚVWXYZŽ"
SECRET_TEXT = "Vo 80 +trtx 8ňw0+o óňzrň ó04p, 6ú y.6í 204ňrú8 6s +7íy Pňs6ň40+ú ůňyóň"

##############################################################
# Caesar - posun každého znaku o jiný počet dle vzoru

def shift_char(char, shift, decrypted=False):
    """Posun znaků o určité množství dle indexu v abecedě."""
    if char in MY_ALPHABET:
        pos = MY_ALPHABET.index(char)
        if decrypted:
            return MY_ALPHABET[(pos - shift) % len(MY_ALPHABET)]
        else:
            return MY_ALPHABET[(pos + shift) % len(MY_ALPHABET)]
    return char

def caesar_cipher_multi_shift(shifts, text, decrypted=False):
    """Použití Caesarovy šifry na úrovni znaků s různým posunem dle vzoru."""
    output = ""
    for i, char in enumerate(text):
        shift = shifts[i % len(shifts)]
        output += shift_char(char, shift, decrypted)
    return output

##############################################################
# Caesar - posun slov ve větě s daným posunem

def caesar_word_shift(text, shift):
    """Posun slov v textu o určité množství."""
    words = text.split()
    shift %= len(words)
    shifted_words = [words[(i + shift) % len(words)] for i in range(len(words))]
    return ' '.join(shifted_words)

def rearrange_sentence(text, shift):
    """Alternativní způsob přesunu slov ve větě."""
    words = text.split()
    shift %= len(words)
    rearranged_words = words[shift:] + words[:shift]
    return ' '.join(rearranged_words)

##############################################################
# Caesar - hrubá síla dešifrování zprávy pomocí známé abecedy

def decrypt_caesar(encrypted_text, shift, alphabet):
    """Dešifrování Caesarovy šifry s daným posunem."""
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text

##############################################################
# Spuštění programu - MAIN

if __name__ == "__main__":
    # Posun jednotlivých znaků dle vzoru
    print("Caesarova šifra s různým posunem znaků\n")
    input_text = input("Zadejte text, ideálně větu nebo souvětí pro zašifrování: ")
    
    shifts = [3, 5, 7]  # Vzor posunu
    print("Vzor pro posun:", shifts)
    
    encrypted_text = caesar_cipher_multi_shift(shifts, input_text)
    print("Zašifrovaný text:", encrypted_text)
    
    decrypted_text = caesar_cipher_multi_shift(shifts, encrypted_text, decrypted=True)
    print("Odšifrovaný text:", decrypted_text)
    print("------------------------------------------------\n")

    # Posun celých slov v textu
    print("Caesarova šifra s posunem slov\n")
    shift = int(input("Zadejte číslo pro posun slov v původní větě: "))
    
    encrypted_text = caesar_word_shift(input_text, shift)
    print("Zašifrovaná věta (posun slov):", encrypted_text)
    
    decrypted_text = caesar_word_shift(encrypted_text, -shift)
    print("Odšifrovaná věta (původní pořadí):", decrypted_text)
    print("------------------------------------------------\n")

    # Alternativní metoda posunu slov
    print("Caesarova šifra s posunem slov - alternativní metoda\n")
    output_sentence = rearrange_sentence(input_text, shift)
    print("Zašifrovaná věta (alternativní posun slov):", output_sentence)
    print("------------------------------------------------\n")

    # Hrubá síla pro rozluštění Caesarovy šifry
    print("Caesar hrubou silou\n")
    print(f"Zašifrovaná věta: {SECRET_TEXT}\n")
    
    for shift in range(len(MY_ALPHABET)):
        decrypted_text = decrypt_caesar(SECRET_TEXT, shift, MY_ALPHABET)
        print(f"Posun {shift}: {decrypted_text}")
