import os
import time

alphabets = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
specials = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
words = ""

phrase = input("Enter a phrase (ex. Hello, World!): ")

start = time.perf_counter()
for word in phrase:
    if word in alphabets:
        charset = alphabets
    elif word in alphabets.upper():
        charset = alphabets.upper()
    elif word in digits:
        charset = digits
    elif word in specials:
        charset = specials

    for char in charset:
            if char == word:
                words += char
                break
            else:
                print(words + char)
            time.sleep(.1)
            os.system("cls")
else:
    end = time.perf_counter()
    print(f"{words}\n\n{end - start:.2f} seconds.")