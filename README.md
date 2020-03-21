# Algebracha 🌶
A simple Python library adding support for basic Linear Algebra and Analytic Geometry operations

## Creating a new matrix object

  ```
  from algebracha import Matrix
  
  matrix = Matrix('1 2 3, 4 5 6')
  ```
  Matrix's constructor requires one string argument that defines the actual matrix: <br>
  EG: to create the following matrix:
  
  | 1 | 2 | 3 | 4 |
  |---|---|---|---|
  | 5 | 6 | 7 | 8 |
  
  The argument string must be:
  ```
  '1 2 3 4, 5 6 7 8'
  
  # or
  
  '''
    1 2 3 4,
    5 6 7 8
  '''
  ``` 
---
## Methods
```
matrix = Matrix('1 0, 0 1')
```

### Check if the matrix is square

###### Returns True if the matrix is square, False otherwise
`matrix.isSquare()` 

### Check if the matrix is diagonal
###### Returns True if the matrix is diagonal, False otherwise. Matrix must be square
`matrix.isDiagonal()`

### Check if matrix is equal to another matrix
###### Returns True if the matrix passed as argument is equal to this matrix, False otherwise
```
otherMatrix = Matrix('1 2, 3 4')
matrix.equals(otherMatrix)
```

### Transpose matrix
###### Transposes the matrix
`matrix.transpose()`

### Sum matrices
###### Sums the matrix passed as argument with this matrix
```
otherMatrix = Matrix('1 2, 3 4')
matrix.sum(otherMatrix)
```

### Multiply matrices
###### Multiply this matrix with the matrix passed as argument using the "row by column" method
```
otherMatrix = Matrix('1 2, 3 4, 5 6, 7 8')
matrix.sum(otherMatrix)
```

### Compute determinant
###### Returns the determinant of the matrix
`matrix.determinant()`

