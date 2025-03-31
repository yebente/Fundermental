Python = "Awesome"

def myfunc():
    global Python
    Python = "Not so awesome"

myfunc()

print(f"Python is " + Python)
