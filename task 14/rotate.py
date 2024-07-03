matrix = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

n = len(matrix)

rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[n - i - 1][n - j - 1] = matrix[i][j]

for row in rotated_matrix:
    print(row)

# Output: 
# 16  15  14  13 
# 12  11  10  9 
# 8   7   6   5 
# 4   3   2   1