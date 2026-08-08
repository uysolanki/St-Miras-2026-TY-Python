class InvalidAgeError(Exception):
    def __init__(self,message):
        super().__init__(message)


age=int(input("Enter Age"))

try:
    if age>18:
        print("Eligible to vote")
    else:
        raise InvalidAgeError("You are a Minor , sorry you cannot Vote")
except InvalidAgeError as e:
    print(e)
finally:
    print("Thank you!!")