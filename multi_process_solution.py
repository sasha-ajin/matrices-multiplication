from multiprocessing import Manager, Process
import random


def multiplication_matrices(matrix1, matrix2):
    def result_row_calculation(
        result,
        row_index,
        matrix_2_columns_quanity,
        matrix_2_rows_quanity,
    ):
        result_row = result[row_index]
        for matrix2_column_index in range(matrix_2_columns_quanity):
            for matrix2_row_index in range(matrix_2_rows_quanity):
                result_row[matrix2_column_index] += (
                    matrix1[matrix1_row_index][matrix2_row_index]
                    * matrix2[matrix2_row_index][matrix2_column_index]
                )
        result[row_index] = result_row

    matrix_1_columns_quanity, matrix_1_rows_quanity = len(matrix1[0]), len(matrix1)
    matrix_2_columns_quanity, matrix_2_rows_quanity = len(matrix2[0]), len(matrix2)
    result_width = matrix_2_columns_quanity
    result_height = matrix_1_rows_quanity
    result = [[0 for width in range(result_width)] for height in range(result_height)]
    with Manager() as manager:
        result_manager = manager.list(result)
        row_calculation_processes = []
        for matrix1_row_index in range(matrix_1_rows_quanity):
            row_calculation_process = Process(
                target=result_row_calculation,
                args=(
                    result_manager,
                    matrix1_row_index,
                    matrix_2_columns_quanity,
                    matrix_2_rows_quanity,
                ),
            )
            row_calculation_process.start()
            row_calculation_processes.append(row_calculation_process)
        for row_calculation_process in row_calculation_processes:
            row_calculation_process.join()
        print(result_manager)


if __name__ == "__main__":
    """First matrix, we will multiplicate"""
    matrix1 = [[random.randrange(1, 10) for width in range(3)] for height in range(3)]

    """Second matrix, we will multiplicate"""
    matrix2 = [[random.randrange(1, 10) for width in range(3)] for height in range(3)]
    five_to_five_1 = [
        [2, 2, 4, 8, 9],
        [1, 9, 9, 5, 6],
        [8, 5, 3, 7, 8],
        [4, 9, 3, 6, 2],
        [4, 1, 4, 6, 3],
    ]
    five_to_five_2 = [
        [7, 6, 3, 4, 5],
        [2, 8, 4, 3, 5],
        [8, 1, 4, 7, 6],
        [3, 6, 5, 6, 1],
        [5, 3, 3, 4, 2],
    ]
    multiplication_matrices(five_to_five_1, five_to_five_2)
