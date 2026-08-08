# Question 5) 
# Change the oops() function to raise an exception you define yourself, called MyError, 
# and pass an extra data item along with the exception.

class MyError(Exception):

    def __init__(self, message, data):
        self.message = message
        self.data = data

def oops():
    raise MyError("Custom Error Occurred", 404)

def catcher():

    try:
        oops()
        
    except MyError as e:
        print("Custom Exception:", e.message)
        print("Extra Data:", e.data)

catcher()
