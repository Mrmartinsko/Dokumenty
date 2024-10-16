import random

# Globální proměnné pro statistiku
CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0

# Funkce pro vygenerování příkladu se dvěma čísly a základními operacemi
def generate_example():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])

    # Vypíše zadání příkladu
    print(f"\nZADÁNÍ PŘÍKLADU: {num1} {operation} {num2}")

    # Vypočítá výsledek podle operace
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2 if num2 != 0 else "undefined"

    return result

# Funkce pro generování příkladů a ověření výsledku
def exercise_generator_simple():
    global CORRECT_ANSWERS, WRONG_ANSWERS

    while True:
        result = generate_example()

        # Zeptá se uživatele na výsledek
        user_input = input("Zadej svůj výsledek (nebo 'q' pro ukončení): ")

        if user_input.lower() == 'q':
            break

        # Ověření správnosti odpovědi
        try:
            user_answer = float(user_input)
            if user_answer == result:
                print("Správně!")
                CORRECT_ANSWERS += 1
            else:
                print(f"Špatně, správný výsledek je {result}")
                WRONG_ANSWERS += 1
        except ValueError:
            print("Neplatný vstup! Zadej číslo nebo 'q'.")

# Celková funkce pro spuštění generátoru příkladů
def example_generator_2numbers():
    print("\nVítej v generátoru příkladů se dvěma čísly!")
    exercise_generator_simple()

    # Výpis statistiky
    print(f"\nKONEC PROGRAMU: {CORRECT_ANSWERS} správných odpovědí, {WRONG_ANSWERS} špatných odpovědí.")

# Spuštění programu
if __name__ == "__main__":
    example_generator_2numbers()
