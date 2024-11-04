# -*- coding: utf-8 -*-
import os
import random
import datetime
import time

# Mazání obrazovky podle operačního systému
if os.name == 'nt':
    os.system("cls")  # Windows
else:
    os.system("clear")  # Unix-like (Linux, MacOS)

# Inicializace náhodného generátoru s aktuálním časem
random.seed(time.time())

# Získání jména a příjmení od uživatele
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

# Seznam pozdravů
greetings = [
    f"Hello {first_name} {surname}",
    f"Hi there, {first_name} {surname}",
    f"What's good, {first_name} {surname}!"
]

# Výběr náhodného pozdravu
random_greeting = random.choice(greetings)
print(random_greeting)

# Pozdrav podle denní doby
time_now = datetime.datetime.now()

if 0 <= time_now.hour < 12:
    print(f"Good Morning, {first_name} {surname}!")
elif 12 <= time_now.hour < 18:
    print(f"Good Afternoon, {first_name} {surname}!")
else:
    print(f"Good Evening, {first_name} {surname}!")
