# Question 3)
# Define a custom exception class which takes a string message as attribute.


class MyException(Exception):

    def __init__(self, message):
        self.message = message

try:
    raise MyException("This is a custom exception.")

except MyException as e:
    print("Exception:", e.message)
