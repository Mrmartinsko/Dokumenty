# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01) greetings_basics.py

Na inputu jméno, příjmení. Na výstupu jeden ze 3 možných pozdravů včetně vstupních informací.
* jak vyčistit terminál
* jak skutečně zajistit náhodnost
* pozdrav podle denní doby
"""



import os
import random
import datetime

os.system("cls")

random.seed()

first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")


print(f"Hello {first_name} {surname}")

greetings = [
    f"Hello {first_name} {surname}",
    f"Hi there, {first_name} {surname}",
    f"What's good, {first_name} {surname}!"
]
print(f"{random.choice(greetings)}")


time_now = datetime.datetime.now()


if time_now.hour > 0 and time_now.hour <= 12:
    print(f"[*] Good Morning! {first_name} {surname}")
elif time_now .hour > 12 and time_now .hour <= 18:
    print(f"Good Afternoon! {first_name} {surname}")
else:
    print(f" Good Evening! {first_name} {surname}")








