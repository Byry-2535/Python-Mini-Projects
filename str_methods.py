# 1. capitalize()
text = "capitalize"
print(text.capitalize())

# 2. casefold()
text = "CASEFolD"
print(text.casefold())

# 3. center()
text = "center"
print(text.center(10, "="))

# 4. count()
text = "count_count_count"
print(text.count("count"))

# 5. encode()
text = "encode"
print(text.encode(encoding="UTF-8", errors="strict"))

# 6. endswith()
text = "endswith"
print(text.endswith("h"))

# 7. expandtabs()
text = "expandtabs\texpandtabs\texpandtabs"
print(text.expandtabs(2))

# 8. find()
text = "find this str"
print(text.find("this"))

# 9. format()
text = "{} is doing: {}"
print(text.format("Cat", "meow"))

# 10. format_map()
text = "Coordinates: ({x}, {y})"
print(text.format_map({"x": 10, "y": -5}))

# 11. index()
text = "index"
print(text.index("e"))

# 12. isalnum()
text = "isalnum123"
print(text.isalnum())

# 13. isalpha()
text = "isalpha"
print(text.isalpha())

# 14. isascci()
text = "isascci"
print(text.isascii())

# 15. isdecimal(), 16. isdigit(), 17. isnumeric() - pass

# 18. isidentifer()
text = "is_identiFier"
print(text.isidentifier())

# 19. islower()
text = "Islower"
print(text.islower())

# 20. isprintable()
text = "isprintable\n"
print(text.isprintable())

# 21. isspace()
text = "     "
print(text.isspace())

# 22. istitle()
text = "Is Title"
print(text.istitle())

# 23. isupper()
text = "ISUPPER"
print(text.isupper())

# 24. join()
print("-".join(["1", "2", "3"]))

# 25. ljust()
text = "ljust"
print(text.ljust(10, "_"))

# 26. lower()
text = "LOWER"
print(text.lower())

# 27. lstrip()
text = "lstrip"
print(text.lstrip("l"))

# 28. maketrans() & 29. translate()
text = "Make Translate"
temp = text.maketrans("M", "B")
print(text.translate(temp))

# 30. partition()
text = "a+b=c"
print(text.partition("="))

# 31. removeprefix()
text = "removeprefix"
print(text.removeprefix("rem"))

# 32. removesuffix()
text = "removesuffix"
print(text.removesuffix("fix"))

# 33. replace()
text = "replace this"
print(text.replace("this", "that"))

# 34. rfind()
text = "rfindr"
print(text.rfind("r"))

# 35. rindex()
text = "rindex()"
print(text.rindex("x"))

# 36. rjust()
text = "rjust"
print(text.rjust(10, "_"))

# 37. rpartition()
text = "a+b=c"
print(text.rpartition("="))

# 38. rsplit()
text = "split this text"
print(text.rsplit())

# 39. split()
text = "Split This Text"
print(text.split())

# 40. rstrip()
text = "rstrip rstrip"
print(text.rstrip("rstrip"))

# 41. splitlines()
text = "split\nlines"
print(text.splitlines())

# 42. startswith()
text = "startswith"
print(text.startswith("s"))

# 43. strip()
text = "-- strip --"
print(text.strip("-"))

# 44. swapcase()
text = "SwapCase"
print(text.swapcase())

# 45. title()
text = "this IS a Title"
print(text.title())

# 46. upper()
text = "upper"
print(text.upper())

# 47. zfill()
text = "zfill"
print(text.zfill(10))