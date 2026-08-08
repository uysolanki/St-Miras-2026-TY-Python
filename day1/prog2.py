try:
    numerator=int(input("Please enter numerator value"))
    denominator=int(input("Please enter denominator value"))

    result=numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Please enter a non zero denominator")
except ValueError:
    print("Please enter an integer value only")

print("Happy Friendship day!!!")

# Total weight of a mixture of sugar and sand is 1.5 kg

# The sand is 1 kg heavier that the sugar

# what is the weight of sugar in the mixture? 250