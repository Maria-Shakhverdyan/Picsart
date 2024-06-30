matrix = []
tox = int(input("toxeri qanak: "))
syun = int(input("syuneri qanak: "))

for i in range(tox):
    row = []
    for j in range(syun):
        element = int(input(f"enter elements [{i + 1}, {j + 1}]: "))
        row.append(element)
    matrix.append(row)

# maximum = max(matrix)

maximum = matrix[0][0]

for i in range(tox):
    for j in range(syun):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

print(maximum)