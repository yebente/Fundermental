# To read and display file content with line numbers
try:
    with open("students.txt", "r") as f:
        print("Contents of students.txt:")
        for i, line in enumerate(f, start=1):
            print(f"{i}. {line.strip()}")
except FileNotFoundError:
    print("students.txt not found.")
except Exception as e:
    print(f"An error occurred while reading: {e}")

print("\n" + "-" * 50 + "\n")