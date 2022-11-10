'''
Author: Mahad Osman
Date Nov 9th
'''
def find_factors(num):
    """Find factors of num, in increasing order.

    >>> xc
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    numList = []
    for n in range(1, num + 1 ):
        #print(n)
        if num % n == 0:
            numList.append(n)
    return numList