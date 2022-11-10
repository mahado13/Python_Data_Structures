from typing import ItemsView

'''
Author: Mahad Osman
Date: Nov 9
'''
def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for el in lst:
       # print(type(el))
        if(isinstance(el , list)):
            status = True
        else:
            status = False
    return status