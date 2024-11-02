# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
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
FILE_NAME = "users.txt"         # název souboru pro credentials file


##############################################################
### Hashování, registrace, login, zápis do souboru FILE_NAME
# funkce hash_password, register_user, login_user
# zaměřit se na vstupy od uživatele a dořešit možné komplikace - není v řešení

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(password,email):
    hashed_password = hash_password(password)
    with open (FILE_NAME, 'a' ) as file:
        file.write(f"{email},{hashed_password}\n")
    print("Registrace byla úspěšná!")


def login_user(password, email):
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
        return False  
    except FileNotFoundError:
        return False  
        


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    # Test registrace/přihlášení
    while True:
      choice = input("\nChcete se registrovat nebo přihlásit? (r/p) nebo q pro ukončení: ").lower()
      if input ==  'q':
          break
      elif input == 'r':
          

