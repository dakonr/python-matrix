from Matrix import *


if __name__ == '__main__':
    test_matrix = Matrix([[1, 2, 3], [1, 2, 3],[1, 2, 3]])
    test_matrix = test_matrix * 2
    test_matrix = 2 * test_matrix
    norm_matrix = Matrix([[0, 0, 1], [0, 1, 0],[1, 0, 0]])
    print(test_matrix.data)
    test_matrix = norm_matrix * test_matrix
    test_matrix.print()
    test_matrix = test_matrix + norm_matrix
    test_matrix.print()