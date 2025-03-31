# Create a variable outside of a function, and use it inside the function

x = "Stan"

def myfunc():
    print("Hello " + x)

myfunc()