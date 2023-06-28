def sum_column_elements(matrix, column_index):
    total = 0
    for row in matrix:
        total += row[column_index]
    return total

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = sum_column_elements(matrix, 2)
print(result)