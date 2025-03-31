# Create a variable outside of a function, and use it inside the function
"""
x = "Stan"

def myfunc():
    print("Hello " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable

y = "Cars"

def myfunc():
    y = "Volvo"
    print(f"I love {y}")

myfunc()
"""

#Create a variable inside a function, with the same name as the global variable
def myfunc():
    global x # This will create a global variable x, and can be accessed outside this function in line 29
    x = "Mbaru" # This will create a local variable x, and cannot be accessed outside this function
    print("I love " + x)

myfunc()

print("I love " + x) # This will raise an error if x is not defined outside the function by global x in line 23