# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""
07_hash_hesla.py

* Hesla od uživatelů NELZE uchovávat jako plain text, proto se pokuste vymyslet hash metodu šifrování hesel.
  Na vstupu bude heslo jako string, na výstupu jeho hash. Doplňte o funkci, která zjistí, jestli uživatel zadá
  stejné heslo jako původní string. Simulace přihlášení do služby po registraci.
* Vytvořte možnost opakované registrace uživatelů s tím, že budou zadávat e-mail a heslo. Tato credentials
  uložte do txt souboru tak, aby nedošlo ke snížení bezpečnosti hesel (hash). Následně rozhodněte, zda se
  uživatel úspěšně přihlásil nebo jeho uživatelské jméno není v souboru nebo jeho heslo nesedí.
* Dořešit ošetření vstupů od uživatele.
"""

import os
import hashlib

# Globální konstanty a proměnné
FILE_NAME = "users.txt"         # název souboru pro credentials


def hash_password(password):
    """
    Vytvoří SHA-256 hash pro dané heslo.

    :param password: heslo jako řetězec, které chceme zahashovat
    :return: hash hesla jako hexadecimální řetězec
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(email, password):
    """
    Registruje nového uživatele pomocí e-mailu a hesla. Heslo je zahashováno a uloženo spolu s e-mailem do textového souboru.

    :param email: e-mail uživatele jako řetězec
    :param password: heslo uživatele jako řetězec
    :return: Žádná návratová hodnota, vypíše potvrzení úspěšné registrace.
    """
    hashed_password = hash_password(password)
    with open(FILE_NAME, 'a') as file:
        file.write(f"{email},{hashed_password}\n")
    print("Registrace byla úspěšná!")


def login_user(email, password):
    """
    Ověří přihlašovací údaje uživatele. Porovná zadaný e-mail a hash hesla s údaji uloženými v souboru.

    :param email: e-mail uživatele jako řetězec
    :param password: heslo uživatele jako řetězec
    :return: True, pokud se e-mail i heslo shodují se záznamem v souboru; jinak False
    """
    hashed_password = hash_password(password)
  
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                stored_email, stored_hash = line.strip().split(',')
                if email == stored_email:
                    if hashed_password == stored_hash:
                        return True
                    else:
                        return False
        return False  # Email nenalezen
    except FileNotFoundError:
        return False  # Soubor neexistuje

##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    # Test registrace/přihlášení
    while True:
        choice = input("\nChcete se registrovat nebo přihlásit? (r/p) nebo q pro ukončení: ").lower()
        
        if choice == 'q':
            break
        elif choice == 'r':
            email = input("Zadejte váš e-mail: ")
            password = input("Zadejte heslo: ")
            register_user(email, password)
        elif choice == 'p':
            email = input("Zadejte váš e-mail: ")
            password = input("Zadejte heslo: ")
            if login_user(email, password):
                print("Přihlášení úspěšné!")
            else:
                print("Neplatné přihlašovací údaje!")
        else:
            print("Neplatná volba, zkuste to znovu.")
