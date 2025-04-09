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