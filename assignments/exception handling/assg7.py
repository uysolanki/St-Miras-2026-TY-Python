# Question 7) 
# Write a text file named test.txt that contains integers, characters and float numbers. 
# Write a Python program to read the test.txt file and print appropriate message using exception.

try:

    file = open("test1.txt", "r")

    print("File Contents:")
    print(file.read())

    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Permission denied while opening the file.")

except Exception as e:
    print("Some other error occurred:", e)

else:
    print("File read successfully.")

finally:
    print("Program Ended.")