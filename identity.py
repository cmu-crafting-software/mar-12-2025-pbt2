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
    matrix = [[0] * n] * n 
    for i in range(n):
        matrix[i][i] = 1

    return matrix