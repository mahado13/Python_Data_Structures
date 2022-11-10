'''
Author: Mahad Osman
Date: Nov 8th
Referenc: https://www.w3schools.com/python/ref_func_all.asp#:~:text=The%20all()%20function%20returns,()%20function%20also%20returns%20True.
'''
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    newNum1 = all([str(num1).count(c) for c in str(num2)])
    newNum2 = all([str(num2).count(c) for c in str(num1)])

    if newNum1 and newNum2:
        return True
    else: 
        return False
    # for i in newNum1:
    #    print(newNum1.count(i))
    #    if (i not in  newNum2):
    #        status= False
    #    else:
    #        status = True
    # return status
