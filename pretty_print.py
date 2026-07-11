import time

start = time.perf_counter()
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specials = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

phrase = input("Enter a phrase (ex. Hello, World!): ")

words = ""
for word in phrase:
    if word in alphabets:
        for char in alphabets:
            if char == word:
                words += char
                break
            else:
                print(words + char)
            time.sleep(.1)
    elif word in digits:
        for char in digits:
            if char == word:
                words += char
                break
            else:
                print(words + char)
            time.sleep(.1)
    elif word in specials:
        for char in specials:
            if char == word:
                words += char
                break
            else:
                print(words + char)
            time.sleep(.1)
else:
    end = time.perf_counter()
    print(f"\nPretty Print: {words}\n{end - start:.2f} seconds.")