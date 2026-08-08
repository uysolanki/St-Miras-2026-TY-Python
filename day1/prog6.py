age=int(input("Enter Age"))

try:
    assert age >= 18, "Age should be 18 or above."
except AssertionError as e:
    print(e)
finally:
    print("Thank you!!")