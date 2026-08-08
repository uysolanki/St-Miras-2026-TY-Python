# Question 1) 
# Write a Python program that tries to access the array element whose 
# index is out of bound ,and handle the corresponding exception.


arr = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element =", arr[index])

except IndexError:
    print("Error: Array index is out of bounds.")

except ValueError:
    print("Please enter a valid integer index.")