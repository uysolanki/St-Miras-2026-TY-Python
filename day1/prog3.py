#       0     1     2
cars=["BMW","Audi","Merc"]
# print(len(cars))
try:
    print(f"I like to drive {cars[10]}")
except IndexError:
    print("Please enter valid index")
finally:
    print("Happy Friendship day")
