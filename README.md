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

## Methods
```
matrix = Matrix('1 0, 0 1')
```

### Check if the matrix is square (bool)
`matrix.isSquare()` 

### Check if the matrix is diagonal (bool)
`matrix.isDiagonal()`

### Check if matrix is equal to another matrix (bool)
```
otherMatrix = Matrix('1 2, 3 4')
matrix.equals(otherMatrix)
```

### Transpose matrix (None)
`matrix.transpose()`


