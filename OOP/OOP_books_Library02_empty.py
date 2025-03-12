

import json
import sys

class Book:
   

    def __init__(self, title: str, author: str, year: int, is_available = True):
            self.title = title
            self.author = author
            self.year = year
            self.is_available = is_available 
            
   
    def __str__(self):
        return f"{self.title} od {self.author} vydána v roce {self.year} ({self.is_available})"
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, NOVA_hodnota):
        if not (1440 <= NOVA_hodnota <= 2025):
            raise ValueError("rok vydání knihy není platný")
        self._year = NOVA_hodnota

    @classmethod
    def from_string(cls, vstup):
        Název, Autor, Rok = vstup.split(";")
        return cls(Název, Autor, int(Rok))

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,  
            "is_available": self.is_available
        }
  
        

class Ebook(Book):
    def __init__(self, title, author, year, fileformat):
        super().__init__(title, author, year)
        self.fileformat = fileformat
    
    def file_format(self):
        return f"{self.title} - {self.author} vydána v {self.year} je v {self.file_format}"
    
    def __str__(self):
        return super().__str__() + f"je ve formátu {self.fileformat}"
    
    
class Audiobook(Book):
    def __init__(self, title, author, year,duration):
        super().__init__(title, author, year)
        self.duration = duration
    def lenght(self):
        return f"{self.title} - {self.author} vydána v {self.year} je dlouhá {self.duration} minut"
    
    def __str__(self):
        return super().__str__() + f"je dlouhá {self.duration} minut"
       
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
    
    def list_books(self):
        for book in self.books:
            print(book)

    
    def save_book(self, file = "book.json"):
        books_list = []
        for book in self.books:
            books_list.append(book.to_dict())
        with open(file, "w", encoding="utf-8") as f:
            json.dump(books_list, f, ensure_ascii=False, indent=4)
        
   
    def load_books(self,file = "book.json"):  
        with open(file, "r", encoding="utf8") as f:
            data = json.load(f)
            for book in data:
                self.books.append(Book(book["title"], book["author"], book["year"], book["is_available"]))
       



def add_new_book(library):
    title = input("Zadejte název knihy: ")
    author = input("Kdo knihu napsal?: ")
    while True:
        try:
            year = int(input("Kdy byla kniha vydána(1440-2025)?: "))
            if  not (1440 <= year <= 2025):
                print("Zadejte znovu rok vydání knihy: ")
            else:
                break
        except ValueError:
            print("Zadejte ČÍSLO")
    book = Book(title, author, year)
    library.add_book(book)

def borrow_book(library):
    title = input("Zadejte název knihy, kterou si chcete vypůjčit: ")
    for book in library.books:
        if book.title.lower() == title.lower():
            if book.is_available:
                book.is_available = False
                print("Vypůjčil jste si knihu")
               
            else:
                print("kniha už je vypůjčena")
            return  
    print("TAKOVOU KNIHU TADY NEMAME")

def return_book(library):
    title = input("Zadejte název knihy, kterou chcete vrátit: ")
    for book in library.books:
        if book.title.lower() == title.lower():
            if not book.is_available:
                book.is_available = True
                print("Kniha byla vrácena")
               
            else:
                print("Tohle nedává smysl, tahle kniha už je vrácena")
            return
        
    print("TAKOVÁ KNIHA TU NIKDY NEBYLA")

def save_and_exit(library, file="book.json"):
    library.save_book(file) 
    print("Vše se uložilo, Nashledanou!")
    sys.exit()  


def main():
    library = Library() 
    
    library.load_books()

    while True:
        print("\n menu knihovny:")
        print("[1] ukaž knihu")
        print("[2] přidej knihu")
        print("[3] pujčit knihu")
        print("[4] vrátit knihu")
        print("[5] ulož a odejdi")

        choice = input("Vyber možnost: ")

        if choice == "1":
            library.list_books()
        elif choice == "2":
            add_new_book(library)
        elif choice == "3":
            borrow_book(library)
        elif choice == "4":
            return_book(library)
        elif choice == "5":
            save_and_exit(library)  
        else:
            print("špatně, znovu: ")

if __name__ == "__main__":
    main()