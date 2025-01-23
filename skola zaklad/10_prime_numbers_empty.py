# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
10_prime_numbers.py

* Napište jednoduchou funkci, která ověří, zda je číslo prvočíslem.
* Nachystejte si i přípravnou funci, která si vyžádá od uživatele přirozené číslo, bude se využívat opakovaně.
* Nalezněte funkci, která vrátí prvočísla až do vloženého n.
* Nalezněte funkci, která vrátí prních n prvočísel.
* Eratosthénovo síto - zjistěje, oč se jedná, jak to funguje a jak jej naprogramovat pro prvočísla do n.
** Pokuste se napsat funkci, do které vložíte jinou funkci a číslo n. Výsledkem bude časová náročnost vnitřní funkce pro n. 
** Eratosthenovo síto - optimalizace pomocí bitového pole
** Eratosthenovo síto - optimalizace pomocí segmentace (import math), využijeme i bitarray optimalizaci 
*** Eratosthenovo síto - optimalizace vynecháním sudých čísel, využijeme i bitarray optimalizaci
*** Eratosthenovo síto - wheel faktorizace a segmented optimalizace 
*** Eratosthenovo síto - multiprocessing optimalizace, bitarray a segmentace 
*** Eratosthenovo síto - rozdíl ve spotřebě paměti
** Eratosthenovo síto - grafická interpretace četnosti

## Výsledky pro test 100 mil. na NTB:
## Eratosthénovo síto klasika pro N=100000000:      Peak paměť = 1010.76 MB,  18.549 s
## Eratosthénovo síto bitarray pro N=100000000:     Peak paměť = 223.26 MB,    5.884 s
## Eratosthénovo síto segmented pro N=100000000:    Peak paměť = 208.49 MB,   12.388 s 
## Eratosthénovo síto parity pro N=100000000:       Peak paměť = 263.10 MB,    7.485 s
## Eratosthénovo síto segm. wheel pro N=100000000:  Peak paměť = 208.49 MB,   29.994 s
## Eratosthénovo síto parallel pro N=100000000:     Peak paměť = 261.79 MB,    5.870 s (=10 thread) 5.299 s (=16 thread)
"""

import os
import time
from bitarray import bitarray                              # optimalizace, pip install bitarray
import math
from math import isqrt
import tracemalloc                                         # výpočet paměťové náročnosti
import matplotlib.pyplot as plt
import numpy as np


##############################################################
### Oveření prvočísla
# Funkce get_positive_integer_input, is_prime 

def get_positive_integer_input(user_prompt="Zadejte přirozené číslo: "):
    """ Vyžádá si vstup od uživatele, ověří přirozené číslo, zopakuje task nebo vrátí hodnotu
    Args:
        user_prompt: zpráva do inputu pro uživatele, vyžádání přirozeného čísla
    Returns:
        vrací přirozené číslo
    """
    
    error_msg = "Chybný vstup, prosím, zadejte přirozené číslo."
    while True:
        try:
            value = int(input(user_prompt))
            if value < 1:
                print(error_msg)
            else:
                return value
        except ValueError:
            print(error_msg)


def is_prime(number: int) -> bool:
    """ Určuje, zda je číslo prvočíslem.
    Funkce ověřuje, zda je zadané přirozené číslo prvočíslem.
    Args:
        number (int): číslo, které se ověřuje jako prvočíslo.
    Returns:
        Pokud je číslo prvočíslem, vrací hodnotu True, jinak False.
    """

    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


##############################################################
### Vypsání prvočísel od 2 až po n
# Funkce find_primes_up_to, print_primes_up_to

def find_primes_up_to(n: int) -> list:
    """Najde všechna prvočísla menší než zadané číslo n.
    Funkce projde čísla menší než n a pro každé ověří, zda je prvočíslem.
    Args:
        n (int): horní mez (číslo n), do kterého chceme nalézt prvočísla.
    Returns:
        list: Seznam všech prvočísel menších než n.
    """

    primes = []
    for number in range(2, n):
        if is_prime(number):
            primes.append(number)
    return primes


def print_primes_up_to(n: int):
    """Vypíše všechna prvočísla menší než zadané číslo n.
    Funkce volá find_primes_up_to, která vrací seznam prvočísel, a tato prvočísla vypíše.
    Args:
        n (int): horní mez (číslo N), do kterého chceme vypsat prvočísla.
    """
    primes = find_primes_up_to(n)
    print(f"Prvočísla menší než {n}: {', '.join(map(str, primes))}")


##############################################################
### Vypsání prvních n prvočísel
# Funkce find_first_n_primes, print_first_n_primes

def find_first_n_primes(n: int) -> list:
    """Najde prvních n prvočísel.
    Funkce postupně kontroluje čísla, dokud nenajde n prvočísel.
    Args:
        n (int): počet prvočísel, která chceme najít.
    Returns:
        list: Seznam prvních N prvočísel.
    """

    primes = []
    number = 2  # začínáme od prvního prvočísla

    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    
    return primes


def print_first_n_primes(n: int):
    """Vypíše prvních n prvočísel.
    Funkce volá find_first_n_primes, která vrací seznam prvních n prvočísel,
    a tato prvočísla vypíše.
    Args:
        n (int): počet prvočísel, která chceme vypsat.
    """

    primes = find_first_n_primes(n)
    print(f"Prvních {n} prvočísel: {', '.join(map(str, primes))}")


##############################################################
### Eratosthenovo síto - spočítat pro n, zjistit časovou náročnost
# Funkce sieve_of_eratosthenes, print_primes_sieve, time_consumption

def sieve_of_eratosthenes(n: int) -> list:
    """Implementace algoritmu Eratosthenovo síto pro nalezení všech prvočísel menších než n.
    Args:
        n (int): Horní mez (číslo n), do které chceme nalézt prvočísla.
    Returns:
        list: Seznam všech prvočísel menších než n.
    """
    
    # Vytvoření pole čísel a předpokládáme, že všechna jsou prvočísla (True)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 a 1 nejsou prvočísla

    # Procházíme čísla od 2 do odmocniny z N
    for number in range(2, int(n**0.5) + 1):
        if sieve[number]:  # Pokud je číslo stále považováno za prvočíslo
            # Vyškrtáme všechny jeho násobky
            for multiple in range(number*number, n + 1, number):
                sieve[multiple] = False

    # Všechna čísla, která zůstala označená jako True, jsou prvočísla
    primes = [num for num in range(2, n + 1) if sieve[num]]
    return primes


def print_primes_sieve(n: int):
    """Vypíše všechna prvočísla menší než n pomocí Eratosthenova síta.
    Args:
        n (int): Horní mez (číslo n), do které chceme vypsat prvočísla.
    """
    primes = sieve_of_eratosthenes(n)
    print(f"Prvočísla menší než {n}: {', '.join(map(str, primes))}")


def time_consumption(funkce, n):
    """ Vrací dobu výpočtu funkce s arg. n, v ms, slouží pro časové náročnosti dané funkce a n"""
    start = time.perf_counter()
    funkce(n)
    return (time.perf_counter() - start)*1000


##############################################################
### Eratosthenovo síto - optimalizace pomocí bitového pole
# Funkce sieve_of_eratosthenes_bitarray

def sieve_of_eratosthenes_bitarray(n: int) -> list:
    """Implementace Eratosthenova síta s použitím bitového pole (bitarray)
    Args:
        n (int): Horní mez (číslo n), do které chceme nalézt prvočísla.
    Returns:
        list: Seznam všech prvočísel menších než n.
    """
    
    # Vytvoříme bitové pole pro uchovávání informací, zda je číslo prvočíslem (True)
    sieve = bitarray(n + 1)
    sieve.setall(True)
    sieve[0] = sieve[1] = False  # 0 a 1 nejsou prvočísla

    # Vyškrtávání násobků
    for number in range(2, int(n**0.5) + 1):
        if sieve[number]:
            sieve[number*number:n+1:number] = False  # Vyškrtáme všechny násobky

    primes = [num for num in range(2, n + 1) if sieve[num]]
    return primes


##############################################################
### Eratosthenovo síto - optimalizace pomocí segmentace (import math), využijeme i bitarray optimalizaci
## (nejde ale o úsporu času, ale úsporu paměti)
# Funkce sieve_segmented

def sieve_segmented(n: int) -> list:
    """Segmentované Eratosthenovo síto pro rozsahy nad velká čísla.
    Args:
        n (int): Horní mez (číslo n), do které chceme nalézt prvočísla.
    Returns:
        list: Seznam všech prvočísel menších než n.
    """

    # nastavení meze pro segmentaci, například pro n=100 to bude 11, takže od 1 do 10
    limit = int(n**0.5) + 1
    primes = sieve_of_eratosthenes_bitarray(limit)       #v primes držíme prvočísla z prvního segmentu (2,3,5,7) 
    
    # nastavení dalšího segmentu: 11-20
    low = limit
    high = 2 * limit
    result_primes = primes.copy()            #result_primes bude výsledné E. síto, vyplníme 1. část prvočísel
    
    while low < n:                          #navyšujeme segmenty, ale hlídáme, ať nepřelezeme přes n
        if high >= n:
            high = n + 1

        sieve = bitarray(high - low)        #nastavujeme další pole na velikost segmentu (poslední segment může být menší)
        sieve.setall(True)

        # přes všecha prvočísla z prvního segmentu (2,3,5,7) procházej další segmenty
        for prime in primes:                
            # proměnná start - náročné na pochopení:
            # hledání nejm. násobku prvočísla v daném segmentu, které ještě není vyškrtáno 
            # (pro prime=2 v segm. 11-20 to je max(4,12) = 12: pak vyškrtáme 12,14,16,18,20)
            # (pro prime 3 v segm. 11-20 to je max(9,12) = 12: pak vyškrtáme 12,15,18)
            # (pro prime 5 v segm. 11-20 to je max(25,15) - netřeba už nic škrtat, 15 a 20 už bylo skrtnuto v před. krocích jako 5tinás. 3ky a 5tinás 4ky)
            # (stejně tak pro prime 7 - 14 už bylo škrtnuto jako sedminásobek dvojky)
            # (proto je tam vždy ta druhá mocnina, nižší násobky už byly vyškrtány jako násobky jiných čísel)
            start = max(prime * prime, low  +  (prime - low%prime)%prime)           
            sieve[start - low:high - low:prime] = False   # v našem posunutém poli škrtej=False násobky prime: sieve[zač:konec:krok]                             

        result_primes.extend([num for num in range(low, high) if sieve[num - low]])    # doplň pouze prvočísla

        # posuň se na další segment (je možné, že high bude víc než n, to se vyřeší na začátku cyklu)
        low = high
        high += limit

    return result_primes


##############################################################
### Eratosthenovo síto - optimalizace vynecháním sudých čísel, využijeme i bitarray optimalizaci
# Funkce sieve_odd_optimized

def sieve_odd_optimized(n: int) -> list:
    """Optimalizované Eratosthenovo síto, které ignoruje sudá čísla.
    Args:
        n (int): Horní mez (číslo n), do které chceme nalézt prvočísla.
    Returns:
        list: Seznam všech prvočísel menších než n.
    """

    if n == 2:
        return [2]
    
    # Vytvoříme pole pro lichá čísla (sudá čísla kromě 2 jsou vynechána)
    sieve_size = (n - 1) // 2  # Pole pouze pro lichá čísla od 3 do N
    sieve = bitarray(sieve_size)
    sieve.setall(True)  # Předpokládáme, že všechna lichá čísla jsou prvočísla

    limit = int(n**0.5) + 1

    # Procházíme pouze lichá čísla
    for i in range(1, (limit // 2) + 1):
        if sieve[i]:  # Pokud je aktuální číslo považováno za prvočíslo
            prime = 2 * i + 1  # Z indexu získáme skutečné číslo
            # Vyškrtáme násobky prvočísla
            for multiple in range(prime * prime // 2, sieve_size, prime):
                sieve[multiple] = False

    # Získáme seznam prvočísel (přidáme 2, a poté všechna lichá prvočísla)
    primes = [2] + [2 * i + 1 for i in range(sieve_size) if sieve[i]]
    return primes


##############################################################
### Eratosthenovo síto - wheel faktorizace a segmented optimalizace
# Funkce segmented_wheel_sieve

def segmented_wheel_sieve(n: int) -> list:
    """Segmentované síto s wheel factorization pro rozsahy nad velká čísla.
    Args:
        n (int): Horní mez (číslo N), do které chceme nalézt prvočísla.
    Returns:
        list: Seznam všech prvočísel menších než N.
    """
    limit = int(math.sqrt(n)) + 1
    primes = []
    primes = sieve_segmented(limit)
    
    # Pattern pro wheel factorization (násobky 2, 3, 5)
    pattern = [1, 7, 11, 13, 17, 19, 23, 29]
    wheel_size = 30
    
    low = limit
    high = 2 * limit
    result_primes = primes.copy()
    
    while low < n:
        if high >= n:
            high = n + 1
        
        sieve = bitarray((high - low))
        sieve.setall(True)

        # Pro každý nalezený prvočíselný vzor z malých prvočísel
        for prime in primes:
            # Najdeme startovní bod pro vyškrtávání násobků
            start = max(prime * prime, low + (prime - low % prime) % prime)
            
            for multiple in range(start, high, prime):
                sieve[multiple - low] = False

        # Přidáme výsledná prvočísla z tohoto segmentu
        result_primes.extend([num for num in range(low, high) if sieve[num - low]])
        
        low = high
        high += limit

    return result_primes




if __name__ == "__main__":
    os.system("cls")

    number = get_positive_integer_input()

    print("------------------------------------------------\n")

    print(is_prime(number))
    print_primes_up_to(number)
    print_first_n_primes(number)

    print("------------------------------------------------\n")

    print_primes_sieve(number)
 
    time_usage = time_consumption(sieve_of_eratosthenes,number)    
    print(f"Eratosthénovo síto, čas výpočtu pro {number}: {time_usage:.0f} ms.")
    
    time_usage = time_consumption(sieve_of_eratosthenes_bitarray,number)    
    print(f"Eratosthénovo síto a bitarray, čas výpočtu pro {number}: {time_usage:.0f} ms.")
 
