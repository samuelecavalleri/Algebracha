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

    # swap two rows
    def swapRows(self, row1, row2):
        row1 -= 1
        row2 -= 1
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]

    # swap two columns
    def swapColumns(self, col1, col2):
        col1 -= 1
        col2 -= 1

        for i in range(0, len(self.matrix)):
            self.matrix[i][col1], self.matrix[i][col2] = self.matrix[i][col2], self.matrix[i][col1]

    #sum rows
    def sumRows(self, row1, row2, multiplier = 1):
        row1 -= 1
        row2 -= 1

        row = []

        for i in range(0, len(self.matrix[0])):
            row.append(self.matrix[row1][i] + (self.matrix[row2][i]) * multiplier)

        self.matrix[row1] = row

    #sum columns
    def sumColumns(self, col1, col2, multiplier = 1):
        col1 -= 1
        col2 -= 1

        for i in range(0, len(self.matrix)):
            self.matrix[i][col1] = self.matrix[i][col1] + (self.matrix[i][col2]) * multiplier

    #multiply row by scalar
    def multiplyRow(self, row, scalar):
        row -= 1

        for i in range(0, len(self.matrix[row])):
            self.matrix[row][i] *= scalar

    #multiply column by scalar
    def multiplyColumn(self, column, scalar):
        column -= 1

        for i in range(0, len(self.matrix)):
            self.matrix[i][column] *= scalar

    #transforsm the matrix to its echelon form using Gaussian Elimination
    def transformEchelon(self):
        #move row with the largest leftmost number on top
        for i in range(0, len(self.matrix)):
            if self.matrix[i][0] > self.matrix[0][0]:
                self.matrix.insert(0, self.matrix.pop(i))

        for row in range(1, len(self.matrix) + 1):
            #make first element of the row become 1
            first = self.matrix[row-1][row-1]
            if first != 0:
                self.multiplyRow(row, 1 / first)
            
            #make first element of other rows become 0
            for nextRow in range(row + 1, len(self.matrix) + 1):
                self.sumRows(nextRow, row, self.matrix[nextRow-1][row-1] * -1)

    #compute the rank
    def rank(self)->int:
        if self.isSquare() and self.determinant() != 0:
            return min(len(self.matrix), len(self.matrix[0]))

        #save original matrix state and transform matrix to its echelon form
        oldForm = self.matrix
        self.transformEchelon()

        #count non-zero rows
        rank = 0
        for row in self.matrix:
            nonZero = True
            for i in row:
                if i != 0:
                    nonZero = False

            if not nonZero:
                rank += 1

        #restore matrix to previous state
        self.matrix = oldForm

        return rank
