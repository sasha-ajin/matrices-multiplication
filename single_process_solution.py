import random


def multiplication_matrices(matrix1, matrix2):
    matrix_1_columns, matrix_1_rows = len(matrix1[0]), len(matrix1)
    matrix_2_columns, matrix_2_rows = len(matrix2[0]), len(matrix2)
    result_width = matrix_2_columns
    result_height = matrix_1_rows
    result = [[0 for width in range(result_width)] for height in range(result_height)]
    for matrix1_row_index in range(matrix_1_rows):
        for matrix2_column_index in range(matrix_2_columns):
            for matrix2_row_index in range(matrix_2_rows):
                result[matrix1_row_index][matrix2_column_index] += (
                    matrix1[matrix1_row_index][matrix2_row_index]
                    * matrix2[matrix2_row_index][matrix2_column_index]
                )
    return result


if __name__ == "__main__":
    """First matrix, we will multiplicate"""
    matrix1 = [[random.randrange(1, 10) for width in range(3)] for height in range(3)]

    """Second matrix, we will multiplicate"""
    matrix2 = [[random.randrange(1, 10) for width in range(3)] for height in range(3)]
    print(multiplication_matrices(matrix1, matrix2))
