people = ["Mario", "Elon", "Trump"]

print(f"Original List: {people}")

# 1. append()
people.append("Luigi")
print(f"\nAppended List: {people}")

# 2. copy()
copied = people.copy() # shallow copy, seperated from the original (1D array only)
print(f"\nCopied List: {copied}")

# 3. count()
luigis = people.count("Luigi")
apples = people.count("Apple")
print(f"\nNo. of Luigis: {luigis}\nNo. of Apples: {apples}")

# 4. extend()
people2 = ["Peach", "Mushroom"]
people.extend(people2)
print(f"\nExtended List: {people}")

# 5. insert()
people.insert(1, "Browser")
print(f"\nInserted List: {people}")

# 6. index()
print(f"\nIndex of Elon: {people.index("Elon")}") # error if not in list

# 7. pop()
popped = people.pop(4)
print(f"\nPopped Element: {popped}")

# 8. remove()
people.remove("Mario") # error if not in list
print(f"\nRemoved Mario: {people}")

# 9. reverse()
people.reverse()
print(f"\nReversed List: {people}")

# 10. sort()
people.sort()
print(f"\nSorted List: {people}")
people.sort(reverse=True)
print(f"Sorted List (reversed): {people}")

# 11. clear()
people.clear()
print(f"\nCleared List: {people}")