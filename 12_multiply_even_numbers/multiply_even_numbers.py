'''
Author: Mahad 
Date: Nov 8th

'''
def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # sum = 1
    # while
    # for num in nums:
    #     if (num % 2 == 0):
    #       sum = sum * num
    #         #return 1
    # return sum 
    sum = 1
    count = 0
    while count < len(nums):
        print(nums[count])
        if (nums[count] % 2 == 0):
            sum = sum * nums[count]
        elif(count == len(nums)):
            print('Only odd numbers', count)
        count = count + 1
    return sum
