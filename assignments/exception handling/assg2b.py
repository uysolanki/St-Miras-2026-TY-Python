#Question 2) Write a Python program to input a positive integer. 
# Display correct message for correct and incorrect input.
# use assert

try:
    num = int(input("Enter a positive integer: "))

    assert num > 0, "Number should be positive"

    print("Correct Input", num)

except (ValueError, AssertionError) as e:
    print("Incorrect Input")