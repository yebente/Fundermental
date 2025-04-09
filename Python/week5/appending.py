# Appending a new student name
def append_student():
    try:
        new_name = input("Enter a new student name to add: ")
        with open("students.txt", "a") as f:
            f.write(new_name + "\n")
        print("Student added successfully!")
    except Exception as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Append operation completed.")

append_student()

print("\n" + "-" * 50 + "\n")