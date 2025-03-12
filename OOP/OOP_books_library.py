# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
OOP_Books_Library_empty.py

# Lekce: Základy tříd v Pythonu – Knihovna

V této lekci se naučíme pracovat s třídami v Pythonu na jednoduchém příkladu správy knih v knihovně. Cílem je pochopit:
- Jak definovat třídu a její atributy
- Jak používat metody třídy
- Jak pracovat s objekty (instancemi třídy)
- Jak používat dunder metody (`__str__` pro textovou reprezentaci)
- Jak ukládat a načítat objekty v seznamu

## Zadání úkolu
Vytvoříme systém pro správu knih v knihovně, který umožní:
1. **Vytvořit třídu `Book`**, která bude obsahovat:
   - `title` (název knihy)
   - `author` (autor knihy)
   - `year` (rok vydání)
   - `available` (dostupnost knihy, výchozí hodnota `True`)
   - Metodu `borrow()`, která označí knihu jako vypůjčenou (`available = False`).
   - Metodu `return_book()`, která označí knihu jako dostupnou (`available = True`).
   - Dunder metodu `__str__`, která vypíše informace o knize v přehledném formátu.

2. **Vytvořit seznam knih** (knihovna) a přidat do něj několik knih.
3. **Implementovat jednoduchý terminálový výpis**, který umožní zobrazit seznam knih a jejich dostupnost.

## Očekávaný výstup v terminálu
    Seznam knih v knihovně:
    1984 - George Orwell (1949) | Stav: Dostupná
    To Kill a Mockingbird - Harper Lee (1960) | Stav: Dostupná   
    Mistr a Markétka - Michail Bulgakov (1967) | Stav: Dostupná  
    Malý princ - Antoine de Saint-Exupéry (1943) | Stav: Dostupná

    --- Test vypůjčení a vrácení knih ---

    Kniha '1984' byla úspěšně vypůjčena.
    Kniha '1984' je již vypůjčená.
    Kniha '1984' byla úspěšně vrácena.
    Kniha '1984' již byla dostupná.

    Aktualizovaný seznam knih v knihovně:
    1984 - George Orwell (1949) | Stav: Dostupná
    To Kill a Mockingbird - Harper Lee (1960) | Stav: Dostupná   
    Mistr a Markétka - Michail Bulgakov (1967) | Stav: Dostupná  
    Malý princ - Antoine de Saint-Exupéry (1943) | Stav: Dostupná
"""

class Book:
    """Třída reprezentující knihu v knihovně.
    Args:
        title (str): Název knihy
        author (str): Autor knihy
        year (int): Rok vydání knihy
    Attributes:
        available (bool): Označuje, zda je kniha dostupná k vypůjčení
    Methods:
        borrow(): Označí knihu jako vypůjčenou
        return_book(): Vrátí knihu zpět jako dostupnou
    """

    def __init__(self, title: str, author: str, year: int):
            self.title = title
            self.author = author
            self.year = year
            self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} vypůjčena")
        else:
            return "Kniha není v knihovně"

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} vrácena")
        else:
            return "Kniha je dostupná"

    
    def __str__(self):
        if self.available == True:
            status = "dostupná"
        else:
            status = "vypůjčená"
        return f"{self.title} od {self.author} vydána v roce {self.year} je {status}"
        


# Seznam knih v knihovně
library = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("Mistr a Markétka", "Michail Bulgakov", 1967),
    Book("Malý princ", "Antoine de Saint-Exupéry", 1943)
]

# Výpis knih v knihovně
print("\nSeznam knih v knihovně:")
for book in library:
    print (book)




# Simulace vypůjčení a vrácení knihy
print("\n--- Test vypůjčení a vrácení knih ---\n")
library[0].borrow()
library[0].borrow()  # Pokus o vypůjčení již vypůjčené knihy
library[0].return_book()
library[0].return_book()  # Pokus o vrácení již dostupné knihy

# Znovu vypíšeme knihovnu po změnách
print("\nAktualizovaný seznam knih v knihovně:")
print("\nSeznam knih v knihovně:")
for book in library:
    print (book)
