from typing import Optional
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    size = len(matrix)
    L, R = 0, size - 1

    while L < R:
        T, B = L, R # top bottom are like L R being a square matrix
        for i in range(R-L):
            # save topleft
            topLeft = matrix[T][L + i]
            # BL to TL
            matrix[T][L + i] = matrix[B - i][L]
            # BR to BL
            matrix[B - i][L] = matrix[B][R - i]
            # TR to BR
            matrix[B][R - i] = matrix[T + i][R]
            # topLeft to TR
            matrix[T + i][R] = topLeft
        L += 1
        R -= 1


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
rotate(matrix)
print(matrix)
