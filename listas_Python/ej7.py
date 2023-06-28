def sum_row_elements(matrix, row_index):
    row = matrix[row_index]
    total = 0
    for element in row:
        total += element
    return total

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = sum_row_elements(matrix, 1)
print(result)