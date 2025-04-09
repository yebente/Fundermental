# Task 1: Creating the students.txt files containing names of students
try:
    with open("students.txt", "w") as f:
        f.write("Yebente\n")
        f.write("Wanjiku\n")
        f.write("Otieno\n")
        f.write("Chebet\n")
        f.write("Mwangi\n")
    print("students.txt created and names written successfully.")
except Exception as e:
    print(f"Error writing to students.txt: {e}")

print("\n" + "-" * 50 + "\n")