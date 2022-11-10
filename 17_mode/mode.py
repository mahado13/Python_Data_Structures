'''
'Author: Mahad '
'Date: Nov 8th
Reference: - https://bobbyhadz.com/blog/python-find-most-common-element-in-list
'''
def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    number = max((nums), key = nums.count)
    print(number)

