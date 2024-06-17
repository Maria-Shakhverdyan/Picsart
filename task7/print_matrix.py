n = int(input("Size of matrix: "))

print(f"Elements of {n*n} matrix:")
elements = list(map(int, input().split()))

if len(elements) != n*n:
    print(f"Count of elements ({len(elements)}) is not correct.")
else:
    matrix = []
    for i in range(n):
        row = elements[i*n:(i+1)*n]
        matrix.append(row)

    print("\nMatrix:")
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
