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

    def test_square(self):
        m = '''
            1 0 0,
            0 1 0,
            0 0 1
        '''
        matrix = Matrix(m)

        self.assertTrue(matrix.isSquare())

if __name__ == '__main__':
    unittest.main()