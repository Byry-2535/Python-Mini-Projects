users = {0: "Mario", 1:"Luigi", 2:"James", 3:"Peach", 4:"Mushroom"}

print(f"Original Dict: {users}")

# 1. keys()
print(f"\nKeys: {users.keys()}")

# 2. values()
print(f"\nValues: {users.values()}")

# 3. pop()
popped = users.pop(0) # key
print(f"\nPopped: {popped}\n{users}")

# 4. popitem()
popped_item = users.popitem() # remove the last, returns a tuple
print(f"\nPopped Item: {popped_item}\n{users}")

# 5. copy()
copied = users.copy() # shallow copy
print(f"\nOriginal: {users}, ID: {id(users)}")
print(f"Copied: {copied}, ID: {id(copied)}")

# 6. get()
print(f"\nIf Exist: {users.get(1)}")
print(f"If Not Exist: {users.get(5, "Not Found")}")
print(f"Current Dict: {users}")

# 7. setdefault()
print(f"\nIf Exist: {users.setdefault(1, "???")}")
print(f"If Not Exist: {users.setdefault(5, "???")}")
print(f"Current Dict: {users}")

# 8. fromkeys()
people = ["Mario", "Luigi", "James"]
from_keys = dict.fromkeys(people, "???")
print(f"\nFrom Keys: {from_keys}")

# 9. items()
print(f"\nItems: {users.items()}\nFor Loop:")
for key, value in users.items():
    print(f"{key}. {value}")

# 10. update()
users.update({6:"New"})
print(f"\nUpdated: {users}")

# 11. clear()
users.clear()
print(f"\nCleared: {users}")