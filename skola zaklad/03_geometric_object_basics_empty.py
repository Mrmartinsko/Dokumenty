# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
03) geometric_object_basics.py

Obvod a obsah trojúhelníku - na vstupu budou délky 3 stran
* Doplňte o podmínky řešitelnosti - vstupní hodnoty (využij definici funkce), trojúhelníková nerovnost
* Podle délek stran urči, zda se jedná o některý ze speciálních případů trojúhelníku.
* Dopočítejte úhly v trojúhelníku, upřesněte popis trojúhelníku i podle vypočítaných úhlů.
* Doplňte poloměr kružnice vepsané i opsané.
** Vytvoř "menu" pro volbu úkolu nebo objektu - jde spíše o princip tvorby volby
** Vykresli trojúhelník.
+ Jak by se daná úloha dala rozšířit na další obrazce? Zamysli se na vhodností, efektivitou, smyslem....
# !!! provést instalaci matplotlib příkazem v terminálu: pip install matplotlib
"""


import math
import os



##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

os.system("cls")


##############################################################
### Základní verze - obvod a obsah trojúhelníku

# Získání vstupu od uživatele
print("ZÁKLADNÍ VERZE: Zadejte délky stran trojúhelníku:")
a = float(input("Zadejte stranu a: "))
b = float(input("Zadejte stranu b: "))
c = float(input("Zadejte stranu c: "))


obvod = a+b+c
s = obvod/2
obsah = math.sqrt(s*(s-a)*(s-b)*(s-c))
r1 = (a*b*c)/(obsah*4)
r2 = obsah/s

##############################################################
### Verze s ověřením vstupu - obvod a obsah trojúhelníku
### Funkce side_input_verification

if a + b > c and b +c > a and a + c > b:
    print(f"obvod je: {obvod}")
    print(f"obsah trojúhelníku je: {obsah}")
    print(f"poloměr kružnice opsané je: {r1}")
    print(f"poloměr kružnice vepsané je: {r2}")
else :
    print("zadali jste špatné délky stran")

if a == b or b == c or  a == c:
    print("jedná se o rovnoramenný trojúhelník")
elif a == b == c:
    print("jedná se o rovnostranný trojúhelník")
else : 
    print("jedná se o různostranný trojúhelník")

    
angle_1 = math.degrees(
    math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    )
angle_2 = math.degrees(
        math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    )
angle_3 = 180 - angle_1 - angle_2  
print(f"Úhly trojúhelníku: {angle_1:.2f}°, {angle_2:.2f}°, {angle_3:.2f}°")

   
if angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
    print("Trojúhelník je pravoúhlý.")
elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
    print("Trojúhelník je tupoúhlý.")
else:
    print("Trojúhelník je ostroúhlý.")



