#Question 2) Write a Python program to input a positive integer. 
# Display correct message for correct and incorrect input.

try:
    num = int(input("Enter a positive integer: "))

    if num <= 0:
        raise ValueError("Number should be positive.")

    print("Correct Input ", num)
except ValueError:
    print("Incorrect Input")