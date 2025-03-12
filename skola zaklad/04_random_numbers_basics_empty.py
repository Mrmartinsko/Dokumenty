# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
04) random_numbers_basics.py

Vygeneruj 2 náhodná čísla od 1 do 10, zvol náhodou operaci, zobraz, zeptej se na výsledek, zkontroluj.
* Přidej opakování, dokud nebude stiknuto "q" nebo "Q"
* Přidej statistiku - počet správných odpovědí / celkem příkladů
** Rozděl hlavní funkci na části tak, aby bylo možno generovat příklady i s více čísly (př.: 5+6-4), stačí operace + a -,
   volbu počtu čísel v příkladu ponech na uživateli
"""

import random
import os

# Globální konstanty a proměnné pro sledování statistiky odpovědí
CORRECT_ANSWERS = 0          # Počet správně zodpovězených odpovědí
WRONG_ANSWERS = 0           # Počet špatně zodpovězených odpovědí

os.system("cls")  # Vyčistí obrazovku (pro Windows)


##############################################################
### Generátor příkladu - 2 čísla a operace, ověření výsledku, zodpovězení, opakování dokud q
# fce generate_example, exercise_generator_simple, celková funkce example_generator_2numbers

def generate_example():
    """Generuje náhodný příklad se dvěma čísly a náhodnou operací (+, -, *, /)."""
    num1 = random.randint(1, 10)  # Generuje první náhodné číslo (1 až 10)
    num2 = random.randint(1, 10)  # Generuje druhé náhodné číslo (1 až 10)

    # Náhodně vybírá operaci mezi sčítáním, odčítáním, násobením a dělením
    operation = random.choice(['+', '-', '*', '/'])

    print(f"\nZADÁNÍ PŘÍKLADU: {num1} {operation} {num2}")  # Zobrazení příkladu uživateli

    # Výpočet výsledku podle vybrané operace
    if operation == '+':
        result = num1 + num2
    elif operation == '-': 
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "undefined (division by zero)"  # Zabraňuje dělení nulou

    return result  # Vrátí výsledek příkladu


def exercise_generator_simple():
    """Generuje příklady pro dvě čísla a kontroluje odpovědi uživatele."""
    global CORRECT_ANSWERS, WRONG_ANSWERS  # Používáme globální proměnné pro statistiku

    while True:
        result = generate_example()  # Generování příkladu

        user_input = input("Zadej svůj výsledek (nebo 'q' pro ukončení): ")  # Uživatelský vstup

        if user_input.lower() == 'q':  # Kontrola, zda uživatel chce ukončit
            break

        try:
            user_answer = float(user_input)  # Převod vstupu na číslo
            if user_answer == result:  # Porovnání odpovědi s výpočtem
                print("Správně!")
                CORRECT_ANSWERS += 1  # Pokud je odpověď správná, přičteme k počtu správných odpovědí
            else:
                print(f"Špatně, správný výsledek je {result}")
                WRONG_ANSWERS += 1  # Pokud je odpověď špatná, přičteme k počtu špatných odpovědí
        except ValueError:
            print("Neplatný vstup! Zadej číslo nebo 'q'.")  # Pokud uživatel nezadá číslo


def example_generator_2numbers():
    """Hlavní funkce pro generování příkladů s dvěma čísly."""
    print("\nVítej v generátoru příkladů se dvěma čísly!")  # Úvodní zpráva
    exercise_generator_simple()  # Zavolání funkce pro generování příkladů se dvěma čísly

    # Zobrazení statistiky na konci
    print(f"\nKONEC PRVNÍ ČÁSTI PROGRAMU: {CORRECT_ANSWERS} správných odpovědí, {WRONG_ANSWERS} špatných odpovědí.")


##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, celková fce example_generator_processor

def numbers_generator(number_count, max = 10):
    """Generuje seznam náhodných čísel pro složitější příklady."""
    numbers = [random.randint(1, max) for _ in range(number_count)]  # Generuje seznam čísel
    return numbers

def example_generator_advance(list_of_numbers):
    """Generuje příklad s více než dvěma čísly a operacemi mezi nimi (+, -)."""
    operators = ['+', '-']  # Seznam operací
    numbers = [random.randint(1, 10) for _ in range(list_of_numbers)]  # Generování čísel
    operations = [random.choice(operators) for _ in range(list_of_numbers - 1)]  # Generování operací mezi čísly

    # Sestavování příkladu jako řetězce
    example = str(numbers[0])
    result = numbers[0]

    for i in range(1, list_of_numbers):
        if operations[i - 1] == '+':
            result += numbers[i]
        else:
            result -= numbers[i]
        example += f" {operations[i - 1]} {numbers[i]}"

    return example, result  # Vrátí sestavený příklad a výsledek


def user_statistics(state: bool):
    """Funkce pro aktualizaci statistik na základě správné/nebo špatné odpovědi."""
    global CORRECT_ANSWERS, WRONG_ANSWERS
    if state:
        CORRECT_ANSWERS += 1  # Pokud je odpověď správná, přičte se k počtu správných odpovědí
    else:
        WRONG_ANSWERS += 1  # Pokud je odpověď špatná, přičte se k počtu špatných odpovědí
    print(f"Správné odpovědi: {CORRECT_ANSWERS}, špatné odpovědi: {WRONG_ANSWERS}")  # Zobrazení statistik


def example_generator_processor():
    """Hlavní funkce pro generování příkladů s libovolným počtem čísel a operací."""
    while True:
        number_of_numbers = input("\nKolik čísel má být v příkladu? Vložte přirozené číslo: ")

        if number_of_numbers.lower() == "q":  # Kontrola ukončení programu
            print("\nProgram byl ukončen.\n")
            exit(0)

        while True:
            try:
                number_of_numbers = int(number_of_numbers)  # Převod vstupu na číslo
                
                if number_of_numbers < 2:
                    print("\nPočet čísel musí být větší než 1. Zadejte prosím znovu.")
                    number_of_numbers = input("\nKolik čísel má být v příkladu? Vložte přirozené číslo: ")
                else:
                    numbers = numbers_generator(number_of_numbers)  # Generování náhodných čísel
                    example, correct_result = example_generator_advance(number_of_numbers)  # Generování příkladu
                    break

            except ValueError:
                print("\nNeplatný vstup. Zadejte prosím celé číslo.")
                number_of_numbers = input("\nKolik čísel má být v příkladu? Vložte přirozené číslo: ")

        print(f"Vypočítej: {example}")  # Zobrazení příkladu

        user_answer = input("Tvůj výsledek (nebo zadej 'q' pro ukončení): ")

        if user_answer.lower() == "q":  # Ukončení programu
            print("\nDěkujeme za procvičování.\n")
            break

        try:
            user_answer = float(user_answer)  # Převod vstupu na číslo
            if abs(user_answer - correct_result) < 0.0001:  # Porovnání odpovědi s výsledkem
                print("Správně!")
                user_statistics(True)  # Aktualizace statistik
            else:
                print(f"Špatně. Správný výsledek je: {correct_result:.2f}")
                user_statistics(False)  # Aktualizace statistik
        except ValueError:
            print("Neplatný vstup, zadej číslo pro počet operací nebo 'q' pro ukončení.")


###########################
