# Let user create or open any file
def user_file_input():
    try:
        file_name = input("Enter the name of the file to open or create: ")
        with open(file_name, "a+") as f:
            f.seek(0)  # Move to the beginning of the file to read
            content = f.read()
            print("Current contents:")
            print(content if content else "[Empty file]")

            print("\nNow add some lines. Type 'done' to finish.")
            while True:
                line = input("> ")
                if line.lower() == "done":
                    break
                f.write(line + "\n")
            print(f"Data saved to {file_name}")
    except Exception as e:
        print(f"Something went wrong: {e}")

user_file_input()