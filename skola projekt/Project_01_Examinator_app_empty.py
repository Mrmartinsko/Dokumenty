# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram



import os
import random
import time
from datetime import datetime


# Globální konstanty a proměnné

MARKING = {
    1:(90, 100),
    2:(75, 90),
    3:(60, 75),
    4:(45, 60),
    5:(0, 45)
}   
os.chdir(os.path.dirname(os.path.abspath(__file__)))
QUESTION_FILE = "martin_svoboda_otazky_smudlinek.txt"
RESULT_FOLDER = "vysledky_testu"

def load_questions_from_directory(directory):
    questions = []
    for filename in os.listdir(directory):
        # Kontrola, zda soubor má příponu .txt
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            try:
                # Otevření souboru a načtení otázek
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Přidání každé otázky do seznamu
                    content = file.read()
                    questions.extend(parse_questions(content, "Autor", filename))
            except Exception as e:
                print(f"Chyba při načítání souboru {filename}: {e}")
    
    # Odstranění prázdných řádků a trimování bílých znaků na začátku a konci
    questions = [question.strip() for question in questions if question.strip()]
    return questions
    
def parse_questions(content, author, filename):
    """Parses the content of a file with questions into a list of dictionaries.
    Args:
        content: str, obsah souboru s otázkami.
        author: str, jméno autora otázek.
        filename: str, název souboru.
    Returns:
        list, seznam otázek ve formě slovníku.
    """
    questions = []
    question_blocks = content.split("Otázka")
    for block in question_blocks[1:]:  
        parts = block.split("x")  
        if len(parts) < 2:
            continue
        
        question_text = parts[1].strip()  

        options_text = parts[2].strip() if len(parts) > 2 else ""
    
        options = [option.strip() for option in options_text.split(";") if option.strip()]
        
        questions_data = {
            'question': question_text,
            'options': options,
            'author': author,
            'filename': filename
             }
        questions.append(questions_data)
    return questions

def shuffle_answers(questions):
    """Zamíchá odpovědi u zadané otázky.    
    Args:
        question: dict, jedna otázka se správnou odpovědí.
    Returns:
        dict, otázka se zamíchanými odpověďmi.
    """
    for question in questions:
        answers = [(answer[:2], answer[2:].strip()) for answer in question['answer']]
        random.shuffle(answers)
        question['answers'] = [f"{mark}{text}" for mark, text in answers]
        question['correct answer'] = next(i for i, (mark, _) in enumerate(answers) if mark == "1;")
    return questions

def get_user_name():
    """Získá jméno a příjmení zadané uživatelem."""
    first_name = input("Zadejte své jméno: ")
    last_name = input("Zadejte příjmení: ")
    return first_name, last_name

def get_number_of_questions(total_questions):
    """Získá od uživatele počet otázek, které chce mít v testu.
    Args:
        total_questions: int, maximální počet dostupných otázek.
    Returns:
        int, počet otázek pro test.
    """
    while True:
        try: 
            number_of_questions = int(input(f"Zadejte počet otázek v rozmezí 1-{total_questions}"))
            if 1 <= number_of_questions >= total_questions:
                return number_of_questions
            else: 
                print("zadejte počet otázek znovu...")
        except ValueError:
            print("zadejte platné číslo")



    
##############################################################
### Spuštění programu - MAIN
if __name__ == "__main__":

    os.system('clear' if os.name == 'posix' else 'cls')
