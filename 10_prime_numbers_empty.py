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

def get_positive_integer_input(inp = "input prime number: "):
    while True:
        try:
            userinput = int(input(inp))
            if userinput < 0:
                print("cislo musi byt kladne")
            else:
                return userinput
        except ValueError:
            print("zadali jste neplatné číslo")

def is_prime(n):
    if n==2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
    

           

    

    

##############################################################
### Vypsání prvočísel od 2 až po n
# Funkce find_primes_up_to, print_primes_up_to
def find_primes_up_to(n):
    primes = []
    for i in range(2,n):
        if is_prime(i):
            primes.append(i)
    return primes

def print_primes_up_to(n):
    primes = find_primes_up_to(n)
    print(f"Prvočísla až do {n} jsou: {primes}")



##############################################################
### Vypsání prvních n prvočísel
# Funkce find_first_n_primes, print_first_n_primes



##############################################################
### Eratosthenovo síto - spočítat pro n, zjistit časovou náročnost
# Funkce sieve_of_eratosthenes, print_primes_sieve, time_consumption



##############################################################
### Eratosthenovo síto - optimalizace pomocí bitového pole
# Funkce sieve_of_eratosthenes_bitarray


##############################################################
### Eratosthenovo síto - optimalizace pomocí segmentace (import math), využijeme i bitarray optimalizaci
## (nejde ale o úsporu času, ale úsporu paměti)
# Funkce sieve_segmented



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


##############################################################
### Eratosthenovo síto - multiprocessing optimalizace, bitarray a segmentace
# Funkce sieve_segment, parallel_sieve

from multiprocessing import Pool

def sieve_segment(start, end, primes_up_to_sqrt):
    """Vyškrtnutí násobků v segmentu."""
    sieve = bitarray(end - start)
    sieve.setall(True)
    
    for prime in primes_up_to_sqrt:
        # Nalezení prvního násobku, který patří do tohoto segmentu
        first_multiple = max(prime * prime, start + (prime - start % prime) % prime)
        sieve[first_multiple - start:end - start:prime] = False

    return [num for num in range(start, end) if sieve[num - start]]

def parallel_sieve(n, num_processes=16):         # nedoporučuji překračovat, pád
    """Paralelizované Eratosthenovo síto."""
    # Nejprve spustíme jednoduché síto pro kořeny
    limit = int(n**0.5) + 1
    primes_up_to_sqrt = sieve_of_eratosthenes_bitarray(limit)

    # Rozdělíme rozsah do segmentů pro paralelní zpracování
    segment_size = (n - limit) // num_processes
    segments = [(i, min(i + segment_size, n)) for i in range(limit, n, segment_size)]

    with Pool(processes=num_processes) as pool:
        segments_primes = pool.starmap(sieve_segment, [(start, end, primes_up_to_sqrt) for start, end in segments])

    # Spojíme všechny výsledky
    result_primes = primes_up_to_sqrt
    for segment_prime in segments_primes:
        result_primes.extend(segment_prime)

    return result_primes


##############################################################
### Eratosthenovo síto - rozdíl ve spotřebě paměti
# measure_sieve_memory

def measure_sieve_memory(function, n, sieve_name="klasika"):
    """Měření paměti pomocí tracemalloc"""
    tracemalloc.start()
    function(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Eratosthénovo síto {sieve_name} pro N={n}: Peak paměť = {peak / 10**6:.2f} MB")


##############################################################
### Eratosthenovo síto - grafická interpretace četnosti
# Funkce plot_prime_distribution



##############################################################
### Spuštění programu - MAIN

if __name__ == "__main__":
    os.system("cls")

    number = get_positive_integer_input()

    print("------------------------------------------------\n")

    print(is_prime(number))
    print_primes_up_to(number)
    print_first_n_primes(number)

    print("------------------------------------------------\n")

#    print_primes_sieve(number)
 
#    time_usage = time_consumption(sieve_of_eratosthenes,number)    
#    print(f"Eratosthénovo síto, čas výpočtu pro {number}: {time_usage:.0f} ms.")
    
#    time_usage = time_consumption(sieve_of_eratosthenes_bitarray,number)    
#    print(f"Eratosthénovo síto a bitarray, čas výpočtu pro {number}: {time_usage:.0f} ms.")
 
#    time_usage = time_consumption(sieve_segmented,number)    
#    print(f"Eratosthénovo síto a segmenty, čas výpočtu pro {number}: {time_usage:.0f} ms.")

#    time_usage = time_consumption(sieve_odd_optimized,number)    
#    print(f"Eratosthénovo síto a parita, čas výpočtu pro {number}: {time_usage:.0f} ms.")

#    time_usage = time_consumption(segmented_wheel_sieve,number)    
#    print(f"Eratosthénovo síto segmented wheel, čas výpočtu pro {number}: {time_usage:.0f} ms.")

#    time_usage = time_consumption(parallel_sieve,number)    
#    print(f"Eratosthénovo síto parallel, čas výpočtu pro {number}: {time_usage:.0f} ms.")

#    print("------------------------------------------------\n")

#    measure_sieve_memory(sieve_of_eratosthenes,number)
#    measure_sieve_memory(sieve_of_eratosthenes_bitarray,number,"bitarray")
#    measure_sieve_memory(sieve_segmented,number,"segmented")
#    measure_sieve_memory(sieve_odd_optimized,number,"parity")
#    measure_sieve_memory(segmented_wheel_sieve,number,"wheel")
#    measure_sieve_memory(parallel_sieve,number,"parallel")
 
#    print("------------------------------------------------\n")
    
#    plot_prime_distribution(number,50)