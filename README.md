# Algebracha 🌶
A simple Python library adding support for basic Linear Algebra and Analytic Geometry operations

## Creating a new matrix object

  ```
  from algebracha import Matrix
  
  matrix = new Matrix('1 2 3, 4 5 6')
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
