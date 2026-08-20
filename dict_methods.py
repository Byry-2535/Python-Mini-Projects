users = {0: "Mario", 1:"Luigi", 2:"James", 3:"Peach", 4:"Mushroom"}

print(f"Original Dict: {users}")

# keys()
print(f"\nKeys: {users.keys()}")

# values()
print(f"\nValues: {users.values()}")

# pop()
popped = users.pop(0) # key
print(f"\nPopped: {popped}\n{users}")

# popitem()
popped_item = users.popitem() # remove the last, returns a tuple
print(f"\nPopped Item: {popped_item}\n{users}")

# copy()
copied = users.copy() # shallow copy
print(f"\nOriginal: {users}, ID: {id(users)}")
print(f"Copied: {copied}, ID: {id(copied)}")

# get()
print(f"\nIf Exist: {users.get(1)}")
print(f"If Not Exist: {users.get(5, "Not Found")}")
print(f"Current Dict: {users}")

# setdefault()
print(f"\nIf Exist: {users.setdefault(1, "???")}")
print(f"If Not Exist: {users.setdefault(5, "???")}")
print(f"Current Dict: {users}")

# fromkeys()
people = ["Mario", "Luigi", "James"]
from_keys = dict.fromkeys(people, "???")
print(f"\nFrom Keys: {from_keys}")

# items()
print(f"\nItems: {users.items()}\nFor Loop:")
for key, value in users.items():
    print(f"{key}. {value}")

# update()
users.update({6:"New"})
print(f"\nUpdated: {users}")

# clear()
users.clear()
print(f"\nCleared: {users}")