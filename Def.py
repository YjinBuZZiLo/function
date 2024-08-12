def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append(n)
        for j in range(m):
            matrix.append(value)
    print(matrix)


result1 = get_matrix(2, 4, 9)
result2 = get_matrix(7, 9, 5)
result3 = get_matrix(1, 8, 6)
print(result1)
print(result2)
print(result3)