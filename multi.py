from multiprocessing import Process, Manager
import random
import os


def multiplication_matrices(matrix1, matrix2):
    def add_element_to_list(
        list, list_column_index, list_row_index, value
    ):
        list[list_column_index][list_row_index] = value

    matrix_1_columns, matrix_1_rows = len(matrix1[0]), len(matrix1)
    matrix_2_columns, matrix_2_rows = len(matrix2[0]), len(matrix2)
    result_width = matrix_2_columns
    result_height = matrix_1_rows
    result = [[0 for width in range(result_width)] for height in range(result_height)]
    for i in range(matrix_1_rows):
        for j in range(matrix_2_columns):
            for k in range(matrix_2_rows):
                add_element_to_list(
                    list=result,
                    list_column_index=i,
                    list_row_index=j,
                    value=matrix1[i][k] * matrix2[k][j],
                )
    return result

if __name__ == "__main__":
    """First matrix, we will multiplicate"""
    matrix1 = [[random.randrange(1, 10) for width in range(3)] for height in range(3)]

    """Second matrix, we will multiplicate"""
    matrix2 = [[random.randrange(1, 10) for width in range(3)] for height in range(3)]
    x = [[1, 2, 3]]
    y = [[4], [5], [6]]
    print(multiplication_matrices(y, x))
    # print(multiplication_matrices(matrix1, matrix2))
