# Dealing with the File Not Found for grades.txt
try:
    with open("grades.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("grades.txt not found. Please create the file first.")
except Exception as e:
    print(f"An error occurred while opening grades.txt: {e}")

print("\n" + "-" * 50 + "\n")