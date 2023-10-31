fryits = ["apple", "banana", "cherry"]
try:
    fryit = "orange"
    index = fryits.index(fryit)
except ValueError:
    print(f"'{fryit}'not found in list")
