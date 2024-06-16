def levenshtein_distance(token1, token2):
    num_of_columns, num_of_rows = (len(token1) + 1, len(token2) + 1)

    matrix = [[0 for _ in range(num_of_columns)] for _ in range(num_of_rows)]

    for i in range(num_of_columns):
        matrix[0][i] = i

    for j in range(num_of_rows):
        matrix[j][0] = j

    for row in range(1, num_of_rows):
        for col in range(1, num_of_columns):
            if token1[col - 1] == token2[row - 1]:
                matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = 1 + min(
                    matrix[row - 1][col],  # Delete
                    matrix[row][col - 1],  # Insert
                    matrix[row - 1][col - 1],  # Replace
                )

    return matrix[num_of_rows - 1][num_of_columns - 1]


def levenshtein_distance_recursive(token1, token2, col=None, row=None):
    # Just for fun
    if col is None:
        col = len(token1)
    if row is None:
        row = len(token2)

    if col == 0:
        return row
    if row == 0:
        return col

    if token1[col - 1] == token2[row - 1]:
        return levenshtein_distance_recursive(token1, token2, col - 1, row - 1)

    return 1 + min(
        levenshtein_distance_recursive(token1, token2, col - 1, row - 1),  # Replace
        levenshtein_distance_recursive(token1, token2, col - 1, row),  # Insert
        levenshtein_distance_recursive(token1, token2, col, row - 1)  # Delete
    )


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))
