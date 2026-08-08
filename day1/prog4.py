#       0     1     2
cars=["BMW","Audi","Merc"]
# print(len(cars))
try:
    print(f"I like to drive {cars[10]}")
except IndexError as e:
    print(e)
finally:
    print("Happy Friendship day")
