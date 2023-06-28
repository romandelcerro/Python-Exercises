def row_with_most_zeros(numbers):
    max_zeros = 0
    row_with_most_zeros = []
    for row in numbers:
        zeros = row.count(0)
        if zeros > max_zeros:
            max_zeros = zeros
            row_with_most_zeros = row
    return row_with_most_zeros

numbers = [[0, 1, 0, 2, 0], [3, 0, 4, 0, 5], [0, 6, 0, 7, 0]]
result = row_with_most_zeros(numbers)
print(result)