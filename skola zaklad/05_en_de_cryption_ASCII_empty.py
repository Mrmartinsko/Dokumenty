import os

def ascii_table():
    print("ASCII PŘEVODNÍK - DEC/CHAR")
    print("Dec  Char")
    for i in range(1, 128):
        print(f"{i:3}  {chr(i):4}")

def ascii_table_with_range(start=32, end=127):
    if start < 0 or end > 127 or start > end:
        print("Chybný rozsah! Musí být mezi 0 a 127.")
        return
    print("ASCII PŘEVODNÍK - DEC/CHAR/BIN/OCT/HEX")
    print(f"{'Dec':<5}{'Char':<5}{'Bin':<10}{'Oct':<5}{'Hex':<5}")
    for i in range(start, end + 1):
        print(f"{i:<5}{chr(i):<5}{bin(i)[2:]:<10}{oct(i)[2:]:<5}{hex(i)[2:].upper():<5}")

def char_to_base(char, base):
    value = ord(char)
    if base == 'bin':
        return bin(value)[2:]
    elif base == 'oct':
        return oct(value)[2:]
    elif base == 'hex':
        return hex(value)[2:].upper()
    else:
        return "Neplatný typ!"

def ascii_table_multicolumn(start=32, end=127, cols=1):
    print(f"{'Dec':<5}{'Char':<5}{'Bin':<10}{'Oct':<5}{'Hex':<5}  " * cols)
    for i in range(start, end + 1, cols):
        for j in range(i, min(i + cols, end + 1)):
            print(f"{j:<5}{chr(j):<5}{bin(j)[2:]:<10}{oct(j)[2:]:<5}{hex(j)[2:].upper():<5}", end='| ')
        print()

if __name__ == "__main__":
    os.system("cls")

    char = "#"
    print(f"Znak '{char}' -> ASCII: ", ord(char))
    print(f"Znak '{char}' -> BIN: ", char_to_base(char, 'bin'))
    print(f"Znak '{char}' -> OCT: ", char_to_base(char, 'oct'))
    print(f"Znak '{char}' -> HEX: ", char_to_base(char, 'hex'))
    print(f"Znak '{char}' -> HIPIIII: ", char_to_base(char, 'hip'))
    print("------------------------------------------------\n")

    ascii_table_multicolumn(35, 62, 4)
