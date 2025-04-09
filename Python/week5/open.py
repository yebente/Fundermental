try:
    f = open("demofile.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'f' in locals() and not f.closed:
        f.close()


# Modern way to open a file using 'with' statement
try:
    with open("demofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
# The file is automatically closed after the block of code is executed.