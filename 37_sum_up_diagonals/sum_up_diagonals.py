'''
Author: Mahad Osman 
Date: Nov 9th
'''
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    topRow = matrix[0]
    bottomRow = matrix[-1]
    print(topRow[0], bottomRow[-1], bottomRow[0], topRow[-1])
    return topRow[0] + bottomRow[-1] + bottomRow[0] + topRow[-1]


# m1 = [1,   2], [30, 40]

#  m2 = [[1, 2, 3],[4, 5, 6],  [7, 8, 9]]