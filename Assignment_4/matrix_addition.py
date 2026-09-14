# Program to perform addition of two matrices

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter elements of first matrix:")
matrix1 = []

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)

print("Enter elements of second matrix:")
matrix2 = []

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

# Add the two matrices
result = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("\nFirst Matrix:")
for row in matrix1:
    print(row)

print("\nSecond Matrix:")
for row in matrix2:
    print(row)

print("\nSum of the two matrices:")
for row in result:
    print(row)
