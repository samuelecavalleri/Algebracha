import unittest
from algebracha.algebracha import Matrix
import math


class TestMatrix(unittest.TestCase):
    def test_create_matrix(self):
        matrix = Matrix('1 2 3, 1 2 3')

        expected = [
            [1, 2, 3],
            [1, 2, 3]
        ]

        self.assertEqual(expected, matrix.toList())

    def test_diagonal(self):
        m = '''
            1 0 0,
            0 1 0,
            0 0 1
        '''
        matrix = Matrix(m)

        self.assertTrue(matrix.isSquare())
        self.assertTrue(matrix.isDiagonal())

    def test_not_diagonal(self):
        m = '''
            1 0 0,
            1 1 0,
            0 0 1
        '''
        matrix = Matrix(m)

        self.assertFalse(matrix.isDiagonal())

    def test_equal(self):
        matrix = Matrix('1 2, 3 4')

        sameMatrix = Matrix('1 2, 3 4')
        differentMatrix = Matrix('1 3, 5 6')

        self.assertTrue(matrix.equals(sameMatrix))
        self.assertFalse(matrix.equals(differentMatrix))

    def test_transpose(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')
        matrix.transpose()

        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        self.assertEqual(expected, matrix.toList())

    def test_sum(self):
        matrix1 = Matrix('1 2, 3 4, 5 6')
        matrix2 = Matrix('1 1, 2 2, 3 3')

        matrix1.sum(matrix2)

        expected = [
            [2, 3],
            [5, 6],
            [8, 9]
        ]

        self.assertEqual(expected, matrix1.toList())

    def test_multiply(self):
        matrix1 = Matrix('4 2, 3 2')
        matrix2 = Matrix('3 2 -4, 5 0 2')

        expected = [
            [22, 8, -12],
            [19, 6, -8]
        ]

        matrix1.multiply(matrix2)

        self.assertEqual(expected, matrix1.toList())

    def test_determinant(self):
        matrix1 = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix2 = Matrix('''
            1 2 3 4 5,
            6 7 8 9 0,
            7 8 9 6 4,
            0 7 1 1 0,
            9 7 8 2 9
        ''')
        self.assertEqual(0, matrix1.determinant())
        self.assertEqual(3455, matrix2.determinant())

    def test_swap_rows(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix.swapRows(1, 3)

        expected = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]

        self.assertEqual(expected, matrix.toList())

    def test_swap_columns(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix.swapColumns(1, 2)

        expected = [
            [2, 1, 3],
            [5, 4, 6],
            [8, 7, 9]
        ]

        self.assertEqual(expected, matrix.toList())

    def test_sum_rows(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix.sumRows(1, 2)
        expected = [
            [5, 7, 9],
            [4, 5, 6],
            [7, 8, 9]
        ]

        self.assertEqual(expected, matrix.toList())

        matrix.sumRows(3, 2, 3)
        expected = [
            [5, 7, 9],
            [4, 5, 6],
            [19, 23, 27]
        ]

        self.assertEqual(expected, matrix.toList())

    def test_sum_columns(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix.sumColumns(1, 2)
        expected = [
            [3, 2, 3],
            [9, 5, 6],
            [15, 8, 9]
        ]

        self.assertEqual(expected, matrix.toList())

        matrix.sumColumns(3, 2, 2)
        expected = [
            [3, 2, 7],
            [9, 5, 16],
            [15, 8, 25]
        ]

        self.assertEqual(expected, matrix.toList())

    def test_multiply_row(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix.multiplyRow(1, 5)

        expected = [5, 10, 15]

        self.assertEqual(expected, matrix.toList()[0])

    def test_multiply_column(self):
        matrix = Matrix('1 2 3, 4 5 6, 7 8 9')

        matrix.multiplyColumn(1, 5)

        expected = [
            [5, 2, 3],
            [20, 5, 6],
            [35, 8, 9]
        ]

        self.assertEqual(expected, matrix.toList())

    def test_echelon(self):
        matrix = Matrix('''
            3 0 1, 
            1 5 2, 
            4 5 4
        ''')

        matrix.transformEchelon()

        expected = [
            [1, 5, 2],
            [0, 1, 1/3],
            [0, 0, 1]
        ]

        testPassed = True

        matrix = matrix.toList()
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if not math.isclose(matrix[i][j], expected[i][j], rel_tol=1e-9):
                    testPassed = False

        self.assertTrue(testPassed)

    def test_rank(self):

        matrix = Matrix('''
            1 2 3,
            3 6 9,
            4 0 4
        ''')

        rank = 2

        self.assertEqual(rank, matrix.rank())

    def test_solve_system(self):

        # given the following linear system of equations
        #   x -5y +z = 0
        #   3x +6y -5z = 1
        #   2x -7y +4z =  4

        matrix = Matrix('''
            1 -5 1 0,
            3 6 -5 1,
            2 -7 4 4 
        ''')

        x = 89/66
        y = 17/33
        z = 27/22

        # print(matrix.solveSystem())
        self.assertEqual([x, y, z], matrix.solveSystem())

if __name__ == '__main__':
    unittest.main()
