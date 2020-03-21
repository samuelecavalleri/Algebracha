class Matrix:

    def __init__(self, rows: str):
        try:
            self.matrix = self._createMatrix(rows)
        except ValueError:
            raise 'Invalid numbers or format'

    # "PRIVATE" FUNCTIONS

    def _createMatrix(self, rows):
        matrix = []

        for row in rows.split(','):
            newRow = []

            for i in row.strip().split(' '):
                newRow.append(float(i.strip()))

            matrix.append(newRow)
            newRow = []

        return matrix

    def _sameSize(self, matrix) -> bool:
        return len(matrix) == len(self.matrix) and len(matrix[0]) == len(self.matrix[0])


    # PUBLIC FUNCTIONS

    # returns the list object representing the matrix
    def toList(self) -> list:
        return self.matrix

    # returns True if the matrix is square
    def isSquare(self) -> bool:
        return len(self.matrix) == len(self.matrix[0])

    # returns True if the matrix is diagonal
    def isDiagonal(self) -> bool:
        if not self.isSquare():
            return False

        size = len(self.matrix)
        for i in range(0, size):
            for j in range(0, size):
                if (i != j and self.matrix[i][j] != 0):
                    return False

        return True

    # returns true if this matrix is equal to the one passed as argument
    def equals(self, matrix) -> bool:
        return matrix.toList() == self.matrix

    # transpose the matrix
    def transpose(self) -> None:
        if not self.isSquare():
            raise Exception('Matrix is not square')

        size = len(self.matrix)

        transposed = [[0 for i in range(0, size)] for j in range(0, size)]

        for i in range(0, size):
            for j in range(0, size):
                transposed[i][j] = self.matrix[j][i]
                print(i, j, transposed)

        self.matrix = transposed

    # sum with the matrix passed as argument
    def sum(self, matrix) -> None:
        matrix = matrix.toList()

        if not self._sameSize(matrix):
            raise Exception('Matrices must have the same dimensions')

        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                self.matrix[i][j] += matrix[i][j]

    # multiply by the matrix passed as argument
    def multiply(self, matrix) -> None:
        matrix = matrix.toList()

        if not len(self.matrix[0]) == len(matrix):
            raise Exception('Matrix passed as argument must have same number of columns as other matrix\'s rows')

        result = [[0 for i in range(0, len(matrix[0]))] for j in range(0, len(matrix))]

        for rowPosition, row in enumerate(self.matrix):
            for i in range(0, len(matrix[0])):
                for j in range(0, len(row)):
                    result[rowPosition][i] += row[j] * matrix[j][i]

        self.matrix = result
        
    # compute the determinant
    def determinant(self) -> float:
        if not self.isSquare():
            raise Exception('Matrix must be square')

        return self._determinant(self.matrix)

    def _determinant(self, matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        size = len(matrix)

        determinant = 0

        for i in range(0, size):
            sign = 1 if (i + 1) % 2 != 0 else -1
            subMatrix = self._subMatrix(matrix, 0, i)
            determinant += matrix[0][i] * self._determinant(subMatrix) * sign

        print(determinant)
        return determinant

    def _subMatrix(self, matrix, row, col):
        size = len(matrix)

        subMatrix = []

        for i in range(0, size):
            if i != row:
                newRow = []
                
                for j in range(0, size):
                    if j != col:
                        newRow.append(matrix[i][j])

                subMatrix.append(newRow)

        return subMatrix



