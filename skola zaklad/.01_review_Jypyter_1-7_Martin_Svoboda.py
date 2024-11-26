# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01_review_Jypyter_1-7.py
Vypracujte bez použití AI a připojení k netu. 12 úkolů.

VYPRACOVAL/A: 
Martin Svoboda
"""

import os

os.system("cls")


##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
    # a) sčítat dvě načtená čísla (suma)
    # b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)

# Načtení čísel
print("numbers")

while True:
    try:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        break
    except ValueError:
        print("invalid input, enter number again: ")
# a) Sčítání
sum = num1 + num2

print(f" summation: {num1} + {num2} = {sum} ")

# b) Dělení a celočíselné dělení
print("division")
while True:
    try:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        break
    except ValueError:
        print("invalid input, enter number again: ")



if num2 != 0:
    share = num1 / num2
    print(f"Division: {num1} / {num2} = {share}")
else:
    share = "not defined"
    print("not defined")



print("full_number division")

while True:
    try:
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        break
    except ValueError:
        print("invalid input, enter number again: ")



if num2 != 0:
    fullshare = num1 // num2
    print(f"full_number_division: {num1} // {num2} = {fullshare}")
else:
    fullshare = "not defined"
    print("not defined")








##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla

# Načtení čísla
print("square root")

while True:
    try:
        num1 = float(input("Enter num1:"))
        break
    except ValueError:
        print("invalid input, enter number again: ")

# a) Třetí odmocnina
sqrt_3 = num1 ** (1/3)

print(f" 3rd square root: {num1}**{1/3} = {sqrt_3} ")
# b) Druhá odmocnina

sqrt_2 = num1 ** (1/2)

print(f" 2nd square root: {num1}**{1/2} = {sqrt_2} ")

##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.
print("3. ukol")

a = int(input("enter your savings: "))
my_savings = a
my_interest = my_savings * 1.1

print(f"my_interest: {my_savings} * {1.1} = {my_interest}")
##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
    # a) načte dva řetězce od uživatele (string1 a string2)
    # b) zkontroluje, zda jsou oba řetězce stejné délky
    # c) spojí oba řetězce do jednoho a vypíše výsledek
print("4. ukol")
# a) Načtení řetězců
string_1 = str(input("enter string1: "))
string_2 = str(input("enter string2: "))

# b) Zkontrolujte délku řetězců
if len(string_1)==len(string_2):
    print("theyre the same")
else :
    print("one is longer")
# c) Spojení řetězců
print("string_1: %s, string_2: %s . "%(string_1, string_2))


##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
    # a) načte číslo od uživatele (např. 16)
    # b) vypíše všechna čísla od 1 do tohoto čísla
    # c) na každém pátém čísle vypíše text "Pátý krok!"
print("5. ukol")
# Načtení čísla
a = int(input("enter number: "))

# b) Výpis čísel
for i in range(1, a+1):
    print(i)
    if i % 5 == 0:
        print("The fifth step")


##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
    # a) vytvoří prázdný slovník "person"
    # b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
    # c) vypíše všechny klíče a hodnoty slovníku v cyklu
print("6. ukol")
# a) Vytvoření slovníku
person = {}

# b) Načtení údajů od uživatele
name = input("enter your name: " )
age = input("enter your age: ")
city = input("enter city: ")
# Přidání údajů do slovníku
person["name"] = name
person["age"] = age
person["city"] = city

# c) Výpis slovníku
print(f"Your name is {person['name']}, you are {person['age']} years old and live in {person['city']}")


##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
    # a) použije f-string pro vložení těchto hodnot do textu
    # b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa
print("7. ukol")
# Načtení čísel
result = float(input("your result: "))
score = float(input("your score: "))

# a) Použití f-string
print(f"Your result is: {result} and youre score is: {score}")

# b) Použití f-string s přesností na 2 desetinná místa
print(f"Your result is: {round(result, 2)} and your score is: {round(score, 2)}")


##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
    # a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
    # b) vypíše třetí prvek seznamu
    # c) vypíše poslední dva prvky seznamu
print("8. ukol")
# a) Vytvoření seznamu
a = input("Prvek 1: ")
b = input("Prvek 2: ")
c = input("Prvek 3: ")
d = input("Prvek 4: ")
e = input("Prvek 5: ")

my_list = [a, b, c, d, e]


# b) Třetí prvek
print(f"Treti prvek je: {c}")

# c) Poslední dva prvky
print(f"Posledni dva prvky seznamu jsou: {d} {e}")

##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
    # a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
    # b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
    # c) seřadí seznam abecedně pomocí metody sort() + zobrazí
print("9. ukol")
# a) Vytvoření seznamu a přidání nového prvku
a = input("Prvek 1: ")
b = input("Prvek 2: ")
c = input("Prvek 3: ")

my_list = [a, b, c]
d = input("Prvek 4: ")
my_list.append(d)

# b) Odstranění prvku na zvoleném indexu
delete = int(input("Ktery z techto 4 prvku chcete odstranit? "))
if 1 <= delete <= 4:  
    my_list.pop(delete - 1)  
else:
    print("Neplatný výběr, zadejte číslo od 1 do 4.")

print(my_list)

# c) Seřazení seznamu
my_list.sort()
print(my_list)


##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
    # a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
    # b) vypíše první prvek tohoto tuple
    # c) vypíše poslední prvek tohoto tuple
print("10. ukol")
# a) Vytvoření tuple
a = input("první prvek: ")
b = input("druhý prvek: ")
c = input("třetí prvek: ")

my_tuple = (a, b, c)
# b) První prvek

print("prvni prvek je:", my_tuple[0])
# c) Poslední prvek

print("Poslední prvek tuple je:", my_tuple[-1])

##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
    # a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
    #    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
    # b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()
print("11. ukol")
# a) Vytvoření tuple a použití metody count()
my_tuple = (1, 2, 3, 2, 4, 2, 5)

prvek = int(input("zadejte prvek: "))
pocet_prvku = my_tuple.count(prvek)

print(f"prvek {prvek} se v tuplu vyskytuje {pocet_prvku}")
# b) Použití metody index()

elemetent_to_find = int(input("zadejte prvek, jehož index chcete zjistit: "))

try:
    index_prvku = my_tuple.index(elemetent_to_find) 
    print(f"prvek {elemetent_to_find} má index {index_prvku}")
except ValueError:
    print(f"prvek {elemetent_to_find} se v tuple nenachází")


    

##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
    # a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
    # b) dokáže zachytit tuto chybu a informovat uživatele o chybě
print("12. ukol")
# a) Vytvoření tuple
my_tuple = (1, 2, 3)

# b) Pokus o změnu prvku
try:
    my_tuple[1] = 178     
except TypeError as e:
    print(f"Chyba: {e}")



##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##