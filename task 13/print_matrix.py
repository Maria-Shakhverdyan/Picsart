matrix = []
n = int(input("enter the size of matrix: "))

for i in range(n):
    row = input(f"enter the elements of row {i + 1} separated by space: ")
    int_row = []
    
    for x in row.split():
        int_row.append(int(x))
    matrix.append(int_row)
    
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
    
