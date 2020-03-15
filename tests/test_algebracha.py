import unittest
from algebracha.algebracha import Matrix


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

if __name__ == '__main__':
    unittest.main()
