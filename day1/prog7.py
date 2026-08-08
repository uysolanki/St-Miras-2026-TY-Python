try:
    num = int(input("Enter a positive integer: "))

    assert num > 0, "Number should be positive"

    print("Correct Input", num)

except (ValueError, AssertionError) as e:
    print("Incorrect Input")