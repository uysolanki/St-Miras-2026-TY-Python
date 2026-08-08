# Question 4) 
# Write a function called oops() that explicitly raises an IndexError exception 
# when called. 
# Then write another function that calls oops() inside a try/except statement 
# to catch the error.



def oops():
    raise IndexError("Index Error generated.")

def catcher():
    try:
        oops()

    except IndexError as e:
        print("Caught Exception:", e)

catcher()