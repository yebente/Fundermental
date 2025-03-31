count = 1

while count <= 20:
    print (f"This is count Number: {count}")
    count += 1

for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")