# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""
08_faktorial.py

* Napište funkci, která vypočítá faktoriál čísla pomocí smyčky for, iterace.
* Napište funkci, která vypočítá faktoriál čísla pomocí rekurze.
* Upravte předchozí funkci tak, aby ošetřovala neplatné vstupy (např. záporná čísla nebo nečíselné hodnoty).
* Porovnejte efektivitu faktoriálu vypočítaného pomocí smyčky a pomocí rekurze pro větší čísla (např. 500). Knihovna time.
* Napište funkce pro výpočet kombinatorických pravidel a vzorců.
* Optimalizujte rekurzivní verzi faktoriálu pomocí memoizace (ukládání výsledků).
* Implementujte přibližný výpočet faktoriálu pomocí Stirlingova vzorce. Ověřte přesnost výpočtů.
* Implementujte detailní měření výpočetního času pro obě verze výpočtu faktoriálu a porovnejte.
"""

import os
import time
import math

# Globální konstanty a proměnné
MEMO = {}  # slovník pro ukládání mezivýsledků, memoizace


def factorial(n):
    """
    Vypočítá faktoriál čísla pomocí smyčky for (iterace).

    :param n: celé kladné číslo pro výpočet faktoriálu
    :return: faktoriál čísla n
    """
    vysledek = 1
    for i in range(1, n + 1):
        vysledek *= i
    return vysledek


def factorial_recurse(n):
    """
    Vypočítá faktoriál čísla pomocí rekurze.

    :param n: celé kladné číslo pro výpočet faktoriálu
    :return: faktoriál čísla n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recurse(n - 1)


def factorial_safe_input(n=None):
    """
    Ošetřuje vstupy pro výpočet faktoriálu – přijímá pouze nezáporná celá čísla.

    :param n: vstupní hodnota, která má být faktoriálem (pouze nezáporná celá čísla)
    :return: hodnota faktoriálu nebo vyvolá výjimku ValueError
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Faktoriál lze vypočítat pouze pro nezáporná celá čísla.")
    
    return factorial(n)


def faktorial_time_consuming(n):
    """
    Porovná časovou náročnost výpočtu faktoriálu pomocí iterativní, rekurzivní a math verze.

    :param n: celé kladné číslo, pro které se měří doby výpočtu faktoriálu
    """
    start = time.perf_counter()
    factorial(n)
    time_iterative = time.perf_counter() - start
     
    start = time.perf_counter()
    factorial_recurse(n)
    time_recurse = time.perf_counter() - start

    start = time.perf_counter()
    math.factorial(n)
    time_math = time.perf_counter() - start

    print(f"Faktoriál čísla {n}")
    print(f"Rekurzivní = {time_recurse*1_000_000:.0f} micro_s")
    print(f"Iterativní = {time_iterative*1_000_000:.0f} micro_s")
    print(f"Math = {time_math*1_000_000:.0f} micro_s")
        
    print(f"Rozdíl v časech rekurzivní - iterativní je {(time_recurse - time_iterative)*1000:.2f} ms.")
    print(f"Rozdíl v časech rekurzivní - math je {(time_recurse - time_math)*1000:.2f} ms.\n")


def permutation(n):
    """
    Vypočítá počet permutací pro `n` prvků.

    :param n: celé číslo, počet prvků
    :return: počet permutací prvků n
    """
    return math.factorial(n)


def combination(n, k):
    """
    Vypočítá kombinace pro výběr `k` prvků z `n`.

    :param n: celé číslo, celkový počet prvků
    :param k: celé číslo, počet vybíraných prvků
    :return: počet kombinací
    """
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def permutation_repetition(n, k):
    """
    Vypočítá permutace s opakováním pro `n` prvků, kde `k` je počet opakujících se prvků.

    :param n: celé číslo, počet prvků
    :param k: celé číslo, počet opakovaných prvků
    :return: počet permutací s opakováním
    """
    return math.factorial(n) // math.factorial(k)


def variation(n, k):
    """
    Vypočítá variace pro `k` prvků vybraných z `n`.

    :param n: celé číslo, celkový počet prvků
    :param k: celé číslo, počet vybíraných prvků
    :return: počet variací
    """
    return math.factorial(n) // math.factorial(n - k)


##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    n = 5
    # Faktoriál pomocí iterace
    print("Faktoriál pomocí cyklu for, iterace:")
    print(f"{n}! = {factorial(n)}")  
    print("------------------------------------------------\n")

    # Faktoriál pomocí rekurze
    print("Faktoriál rekurzivně:")
    print(f"{n}! = {factorial_recurse(n)}")  
    print("------------------------------------------------\n")

    # Faktoriál s kontrolou vstupu
    print("Faktoriál bezpečně:")
    print(f"{n}! = {factorial_safe_input(n)}")  
    try:
        print(f"ahoj! = {factorial_safe_input('ahoj')}")  
    except ValueError as e:
        print(e)
    try:
        print(f"(-20)! = {factorial_safe_input(-20)}")
    except ValueError as e:
        print(e)
    try:
        print(f"3.7! = {factorial_safe_input(3.7)}")
    except ValueError as e:
        print(e)
    print("------------------------------------------------\n")

    # Srovnání časové náročnosti různých metod
    faktorial_time_consuming(50)
    print("------------------------------------------------\n")

    # Příklady použití - kombinatorika - výpočty
    n = 5
    k = 3
    print(f"Počet permutací {n} prvků je: {permutation(n)}")
    print(f"Počet kombinací {k} prvků z {n} je: {combination(n, k)}")
    print(f"Počet permutací s opakováním je: {permutation_repetition(n, k)}")
    print(f"Počet variací {k} prvků z {n} je: {variation(n, k)}")
    print("------------------------------------------------\n")
