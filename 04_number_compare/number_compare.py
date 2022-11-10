'''
Author: Mahad 
Date: Nov 8th
'''
def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if(a >b ):
        return print(f"The first number: {a} is greater than second number: {b}")
    elif(b>a):
        return print(f"The second number: {b} is greater than the first number: {a}")
    else:
        return print(f"{a} and {b} are equal")