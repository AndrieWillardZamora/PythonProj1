
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_sum = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            diagonal_sum += matrix[i][j]

print("Sum of diagonal elements:", diagonal_sum)