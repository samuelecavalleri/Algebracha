from .utils import printMatrix

class Matrix:

    def __init__(self, rows: str):
        try:
            self.matrix = self._createMatrix(rows)
        except ValueError:
            print('Invalid numbers or format')
            raise

    def _createMatrix(self, rows):
        matrix = []

        for row in rows.split(','): 
            newRow = []
            
            for i in row.strip().split(' '): 
                newRow.append(float(i.strip()))

            matrix.append(newRow)
            newRow = []

        return matrix

    # returns the list object representing the matrix
    def toList(self) -> list:
        return self.matrix

    # returns True if the matrix is square
    def isSquare(self) -> bool:
        return len(self.matrix) == len(self.matrix[0])

