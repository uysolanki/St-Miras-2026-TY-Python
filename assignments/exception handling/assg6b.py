# Question 6) 
# Define a class Date(Day, Month, Year) with functions to accept and display it. 
# Accept date from user. Throw user defined exception InvalidDateException if the date is invalid.


class InvalidDateException(Exception):
    pass

class Date:

    def accept(self):
        self.day = int(input("Enter Day: "))
        self.month = int(input("Enter Month: "))
        self.year = int(input("Enter Year: "))

    def validate(self):

        if self.month < 1 or self.month > 12:
            raise InvalidDateException("Invalid Month")

        if self.day < 1 or self.day > 31:
            raise InvalidDateException("Invalid Day")

        if self.month in [4, 6, 9, 11] and self.day > 30:
            raise InvalidDateException("This month has only 30 days")

        if self.month in [1, 3, 5, 7, 8, 10, 12] and self.day > 31:
                    raise InvalidDateException("This month has only 31 days")
        if self.month == 2:
            leap = (self.year % 4 == 0)

            if leap:
                if self.day > 29:
                    raise InvalidDateException(f"February in {self.year} has only 29 days")
            else:
                if self.day > 28:
                    raise InvalidDateException(f"February in {self.year} has only 28 days")

    def display(self):
        print("Date:", self.day, "/", self.month, "/", self.year)


d = Date()

try:
    d.accept()
    d.validate()
    d.display()

except InvalidDateException as e:
    print("Exception:", e)
except ValueError:
    print("Please enter a valid integer value.")