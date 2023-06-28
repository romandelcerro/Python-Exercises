def sum_matrix_elements(matrix):
    total = 0
    for element in matrix:
        total += element
    return total

matrix = [1, 2, 3, 4, 5]
result = sum_matrix_elements(matrix)
print(result)