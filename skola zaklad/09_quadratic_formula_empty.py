# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""
09_quadratic_formula.py

* Program pro výpočet kořenů kvadratické rovnice na základě zadaných koeficientů.
* Program ošetřuje výpočty v oboru reálných i komplexních čísel.
* Obsahuje funkci pro výpočet diskriminantu a výpočet kořenů pomocí Viettových vztahů.
* Generování náhodné kvadratické rovnice a její řešení pro procvičování studentů.
"""

import os
import random
import math
import cmath
import time


def get_coefficients():
    """
    Načte od uživatele koeficienty a, b, c kvadratické rovnice ve tvaru ax^2 + bx + c = 0.

    :return: hodnoty a, b a c zadané uživatelem (typ float)
    """
    a = float(input("Vložte první koeficient (a) kvadratické rovnice (ax^2 + bx + c = 0): "))
    b = float(input("Vložte druhý koeficient (b) kvadratické rovnice (ax^2 + bx + c = 0): "))
    c = float(input("Vložte třetí koeficient (c) kvadratické rovnice (ax^2 + bx + c = 0): "))
    return a, b, c


def calculate_discriminant(a, b, c):
    """
    Vypočítá diskriminant kvadratické rovnice na základě koeficientů a, b a c.

    :param a: koeficient u x^2
    :param b: koeficient u x
    :param c: konstantní člen
    :return: hodnota diskriminantu (typ float)
    """
    return b ** 2 - 4 * a * c


def solve_quadratic_equation():
    """
    Řeší kvadratickou rovnici v oboru reálných čísel. Výpočet se provádí na základě diskriminantu.
    
    :return: kořeny rovnice nebo informaci o neexistujících řešeních
    """
    a, b, c = get_coefficients()
    discriminant = calculate_discriminant(a, b, c)
    if discriminant < 0:   
       return print("Diskriminant je menší než 0, rovnice nemá řešení v reálných číslech.")
    elif discriminant == 0:
        return print(f"Diskriminant je 0, rovnice má jeden reálný kořen: {-b / (2 * a)}")
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"První kořen je {x1} a druhý kořen je {x2}")
        return x1, x2


def solution_finder_quadratic_complex():
    """
    Řeší kvadratickou rovnici v oboru komplexních čísel. Využívá knihovnu `cmath` pro výpočty
    při záporném diskriminantu.
    
    :return: komplexní kořeny kvadratické rovnice
    """
    a, b, c = get_coefficients()
    discriminant = calculate_discriminant(a, b, c)
    if discriminant < 0:   
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"První kořen je {x1} a druhý kořen je {x2}")
        return x1, x2
    elif discriminant == 0:
        return print(f"Diskriminant je 0, rovnice má jeden kořen: {-b / (2 * a)}")
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"První kořen je {x1} a druhý kořen je {x2}")
        return x1, x2


def find_roots_Vieta():
    """
    Rozkládá kvadratický trojčlen pomocí Vietových vztahů na součin tvaru (x - x1)(x - x2).
    
    :return: textový řetězec s rozkladem trojčlenu pomocí Vietových vztahů nebo informaci o
             neexistujících reálných řešeních.
    """
    a, b, c = get_coefficients()
    discriminant = calculate_discriminant(a, b, c)
    if discriminant < 0:
        print("Diskriminant je záporný, rovnice nemá reálné kořeny.")
        return

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    viet_form = f"{a}(x - {x1:.2f})(x - {x2:.2f})"
    print("Rozklad pomocí Vietových vztahů:", viet_form)
    return viet_form


def generate_quadratic_equations():
    """
    Generuje náhodnou kvadratickou rovnici s kořeny a řeší ji. Koeficienty `a`, `b`, a `c`
    jsou generovány náhodně.
    
    :return: textový výpis náhodné kvadratické rovnice a jejích řešení.
    """
    random.seed(time.time()) 
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    equation = f"({a} * x^2) + ({b} * x) + {c} = 0" 
    print("Vygenerovaná rovnice:", equation)
    print("Řešení rovnice:")

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:   
       return print("Diskriminant je menší než 0, rovnice nemá reálné řešení.")
    elif discriminant == 0:
        return print(f"Diskriminant je 0, rovnice má jeden reálný kořen: {-b / (2 * a)}")
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"První kořen je {x1} a druhý kořen je {x2}")  


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    print("Řešení kvadratické rovnice v reálných číslech:")
    solve_quadratic_equation()
    print("------------------------------------------------\n")

    print("Rozklad kvadratické rovnice pomocí Vietových vztahů:")
    find_roots_Vieta()
    print("------------------------------------------------\n")

    print("Vygenerovaná náhodná kvadratická rovnice a její řešení:")
    generate_quadratic_equations()
