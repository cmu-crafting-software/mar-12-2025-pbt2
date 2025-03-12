def create_zero_matrix(rows, cols):
  """
  Creates a matrix with the specified number of rows and columns, filled with zeros.

  Args:
    rows: The number of rows in the matrix.
    cols: The number of columns in the matrix.

  Returns:
    A list of lists representing the matrix, or None if rows or cols are invalid.
  """

  if rows <= 0 or cols <= 0:
    return None  # Handle invalid input

  matrix = [[0 for _ in range(cols)] for _ in range(rows)]
  return matrix

# Adapted from: https://rosettacode.org/wiki/Identity_matrix#Python
#
# This function returns an identity matrix of n x n size such that:
#   n = 1 => [[1]],
#   n = 2 => [[1,0],[0,1],
#   n = 3 => [[1,0,0],[0,1,0],[0,0,1]],
#   ... and so on ...
#
# @param n finite integer >=1
# @returns identity matrix of n x n size
def identity(n):
    matrix = create_zero_matrix(n, n)
    for i in range(n):
        matrix[i][i] = 1

    return matrix