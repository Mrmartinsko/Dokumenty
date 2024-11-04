# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
    02) calc_basics.py

    Vyžádej si na vstupu 2 čísla, proveď s nima základní operace, na výstupu vždy zobraz operaci a výsledek.
    * ošetři dělení nulou
    * ošetři číselný vstup
    ** ukládání výstupů do souboru
    *** GUI tkinter
"""

# import knihoven je zvykem definovat na začátku
import os
import csv

import tkinter as tk
from tkinter import messagebox


os.system('cls')



while True:
    try:
        num1 = float(input("Zadejte číslo:"))
        num2 = float(input("Zadejte číslo:"))
        break
    except ValueError:
        print("zadejte číslici")

sum = num1 + num2
odč = num1 - num2
mult = num1 * num2


print(f" součet: {num1} + {num2} = {sum} ")
print(f" rozdíl: {num1} - {num2} = {odč} ")
print(f" součin: {num1} * {num2} = {mult} ")

if num2 != 0:
    share = num1 / num2
    print(f"podíl: {num1} / {num2} = {share}")
else:
    share = "not defined"
    print(  "podíl: nulou dělit nelze")