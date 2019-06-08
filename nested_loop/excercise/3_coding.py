n = input()

symbol_count = 0
char_int = 0 # the value of the int in specific position

for symbol in range(len(n), 0, -1):
    symbol_count = symbol - 1
    char_int = int(n[symbol_count])
    if char_int == 0:
        print("ZERO")
    else:
        print(chr(char_int + 33) * char_int)