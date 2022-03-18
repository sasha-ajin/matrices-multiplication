from multiprocessing import Manager, Process, Queue
import random
import time


def multiplication_matrices(matrix1, matrix2):
    def item_calculation(index, mul1, mul2, queue):
        queue.put({"index": index, "result": mul1 * mul2})

    def result_row_calculation(
        result,
        row_index,
        matrix_2_columns_quanity,
        matrix_2_rows_quanity,
    ):
        queue = Queue()
        result_row = result[row_index]
        item_calculation_processes = []
        for matrix2_column_index in range(matrix_2_columns_quanity):
            for matrix2_row_index in range(matrix_2_rows_quanity):
                item_calculation_process = Process(
                    target=item_calculation,
                    args=(
                        matrix2_column_index,
                        matrix1[matrix1_row_index][matrix2_row_index],
                        matrix2[matrix2_row_index][matrix2_column_index],
                        queue,
                    ),
                )
                item_calculation_process.start()
                item_calculation_processes.append(item_calculation_process)
        for item_calculation_process in item_calculation_processes:
            item_calculation_process.join()
        while not queue.empty():
            item = queue.get()
            result_row[item["index"]] += item["result"]
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
    multiplication_matrices(matrix1, matrix2)
