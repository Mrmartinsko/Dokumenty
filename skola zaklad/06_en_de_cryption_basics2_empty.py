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

def shift_char(char, shift, decrypted=False):
    """
    Posune daný znak `char` o určitou hodnotu `shift` v rámci MY_ALPHABET.
    Pokud je `decrypted` True, provádí opačný posun (pro dešifrování).

    :param char: znak k posunutí
    :param shift: hodnota posunu
    :param decrypted: logická hodnota určující, zda má být text dešifrován
    :return: posunutý znak nebo původní znak, pokud není v MY_ALPHABET
    """
    if char in MY_ALPHABET:
        pos = MY_ALPHABET.index(char)
        if decrypted:
            return MY_ALPHABET[(pos - shift) % len(MY_ALPHABET)]
        else:
            return MY_ALPHABET[(pos + shift) % len(MY_ALPHABET)]
    return char

def caesar_cipher_multi_shift(shifts, text, decrypted=False):
    """
    Šifruje nebo dešifruje text pomocí Caesarovy šifry s různými posuny pro každý znak.

    :param shifts: seznam posunů pro každý znak
    :param text: text k zašifrování nebo dešifrování
    :param decrypted: logická hodnota určující, zda má být text dešifrován
    :return: šifrovaný nebo dešifrovaný text
    """
    output = ""
    for i, char in enumerate(text):
        shift = shifts[i % len(shifts)]
        output += shift_char(char, shift, decrypted)
    return output

def caesar_word_shift(text, shift):
    """
    Posune slova v textu o zadaný posun `shift`.

    :param text: text k úpravě
    :param shift: hodnota posunu slov
    :return: text s posunutými slovy
    """
    words = text.split()
    shift %= len(words)
    shifted_words = [words[(i + shift) % len(words)] for i in range(len(words))]
    return ' '.join(shifted_words)

def rearrange_sentence(text, shift):
    """
    Alternativně posune slova ve větě dle zadaného `shift`.

    :param text: text k úpravě
    :param shift: hodnota posunu slov
    :return: text s alternativně posunutými slovy
    """
    words = text.split()
    shift %= len(words)
    rearranged_words = words[shift:] + words[:shift]
    return ' '.join(rearranged_words)

def decrypt_caesar(encrypted_text, shift, alphabet):
    """
    Dešifruje Caesarovu šifru daným posunem `shift` a použitou `alphabet`.

    :param encrypted_text: šifrovaný text
    :param shift: hodnota posunu
    :param alphabet: abeceda použitá pro šifrování
    :return: dešifrovaný text
    """
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index - shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char
    return decrypted_text

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
