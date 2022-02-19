from multiprocessing import Process
import random


def multiplication_matrices(matrix1, matrix2):
    result_width = len(matrix2[0])
    result_height = len(matrix1)
    result = [[0 for width in range(result_width)] for height in range(result_height)]
    # iterate through rows of matrix1
    for i in range(len(matrix1)):
        # iterate through columns of matrix2
        for j in range(len(matrix2[0])):
            # iterate through rows of matrix2
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


if __name__ == "__main__":
    """First matrix, we will multiplicate"""
    matrix1 = [[random.randrange(1, 10) for width in range(5)] for height in range(5)]

    """Second matrix, we will multiplicate"""
    matrix2 = [[random.randrange(1, 10) for width in range(5)] for height in range(5)]
    print(multiplication_matrices(matrix1, matrix2))
