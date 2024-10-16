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


# Globální konstanty a proměnné
CORRECT_ANSWERS = 0          # využito ve funkci statistika() ve 2. části
WRONG_ANSWERS = 0           # využito ve funkci statistika() ve 2. části


os.system("cls")


##############################################################
### Generátor příkladu - 2 čísla a operace, ověření výsledku, zodpovězení, opakování dokud q
# fce generate_example, exercise_generator_simple, celková funkce example_generator_2numbers


def generate_example():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    operation = random.choice(['+', '-', '*', '/'])

    print(f"\nZADÁNÍ PŘÍKLADU: {num1} {operation} {num2}")

    if operation == '+':
        result = num1 + num2
    elif operation == '-': 
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "undefined (division by zero)"

        return result
    

def exercise_generator_simple():
    global CORRECT_ANSWERS, WRONG_ANSWERS

    while True:
        result = generate_example()

       
        user_input = input("Zadej svůj výsledek (nebo 'q' pro ukončení): ")

        if user_input.lower() == 'q':
            break

        try:
            user_answer = float(user_input)
            if user_answer == result:
                print("Správně!")
                CORRECT_ANSWERS += 1
            else:
                print(f"Špatně, správný výsledek je {result}")
                WRONG_ANSWERS += 1
        except ValueError:
            print("Neplatný vstup! Zadej číslo nebo 'q'.")


def example_generator_2numbers():
    print("\nVítej v generátoru příkladů se dvěma čísly!")
    exercise_generator_simple()

   
    print(f"\nKONEC PRVNÍ ČÁSTI ROGRAMU: {CORRECT_ANSWERS} správných odpovědí, {WRONG_ANSWERS} špatných odpovědí.")



##############################################################
### Generátor příkladů - n čísel a operace mezi nimi (+, -), přidána funkce statistika
# funkce numbers_generator, example_generator_advance, user_statistics, celková fce example_generator_processor

def numbers_generator(number_count, max = 10):
    numbers = [random.randint(1, max) for _ in range(number_count)]
    return numbers

def example_generator_advance(list_of_numbers):
    operators = ['+', '-']
    numbers = [random.randint(1, 10) for _ in range(list_of_numbers)]
    operations = [ random.choice(operators) for _ in range (list_of_numbers - 1)]

    example = str(numbers[0])
    result = numbers[0]

    for i in range(1, list_of_numbers):
        if operations[i - 1] == '+':
            result += numbers[i]
        else:
            result -= numbers[i]
        example += f" {operations[i - 1]} {numbers[i]}"

    return example, result

def user_statistics(state: bool):
    global CORRECT_ANSWERS, WRONG_ANSWERS
    if state:
        CORRECT_ANSWERS += 1
    else:
        WRONG_ANSWERS += 1
    print(f"Správné odpovědi: {CORRECT_ANSWERS}, špatné odpovědi: {WRONG_ANSWERS}")  

def example_generator_processor():
    while True:
        number_of_numbers = input("\nKolik čísel má být v příkladu? Vložte přirozené číslo: ")

        if number_of_numbers.lower() == "q":
            print("\nProgram byl ukončen.\n")
            exit(0)

        while True:
            try:
                number_of_numbers = int(number_of_numbers)
                
                if number_of_numbers < 2:
                    print("\nPočet čísel musí být větší než 1. Zadejte prosím znovu.")
                    number_of_numbers = input("\nKolik čísel má být v příkladu? Vložte přirozené číslo: ")
                else:
                    numbers = numbers_generator(number_of_numbers)
                    example, correct_result = example_generator_advance(number_of_numbers)
                    break

            except ValueError:
                print("\nNeplatný vstup. Zadejte prosím celé číslo.")
                number_of_numbers = input("\nKolik čísel má být v příkladu? Vložte přirozené číslo: ")

        print(f"Vypočítej: {example}")

        user_answer = input("Tvůj výsledek (nebo zadej 'q' pro ukončení): ")

        if user_answer.lower() == "q":
            print("\nDěkujeme za procvičování.\n")
            break

        try:
            user_answer = float(user_answer)
            if abs(user_answer - correct_result) < 0.0001: 
                print("Správně!")
                user_statistics(True)
            else:
                print(f"Špatně. Správný výsledek je: {correct_result:.2f}")
                user_statistics(False)
        except ValueError:
            print("Neplatný vstup, zadej číslo pro počet operací nebo 'q' pro ukončení.")





    


##############################################################
### Spuštění programu - MAIN
"""
Následující podmínka (if __name__ == "__main__":) zajistí, že se kód v bloku pod touto podmínkou spustí pouze tehdy, 
když je skript spuštěn přímo. Pokud je soubor importován do jiného skriptu, kód v tomto bloku se nespustí.
Jinými slovy lze celý tento soubor v případě potřeby importovat do jiného, hlavního souboru.

__name__ je speciální proměnná, kterou Python automaticky nastaví, až když se skript spouští.
Pokud skript spouštíte přímo jako hlavní program/soubor (např. python muj_skript.py), proměnná __name__ bude mít hodnotu "main".
vs.
pokud skript importujete do jiného skriptu (např. import 04_random_numbers_basics.py), __name__ bude mít hodnotu název souboru 
(zde "04_random_numbers_basics").
"""
if __name__ == "__main__":
    random.seed()
    print("\nPRVNÍ ČÁST PROGRAMU")
    example_generator_2numbers()
    print("------------------------------------------------")
    print("DRUHÁ ČÁST PROGRAMU")
    example_generator_processor()
    print(f"Odpovědi: ve druhé části programu bylo zodpovězeno {CORRECT_ANSWERS} správně a {WRONG_ANSWERS} špatně.\n")
