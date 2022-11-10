def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0
    if(start != 0):
       print('Start point has been indicated')
       if(end == None):
        for num in nums[start::]:
            print(num)
            sum += num 
        return sum
       else:
        for num in nums[start:end + 1:]:
            print(num)
            sum += num 
        return sum
    else:
        if(end ==None):
            print('There is no start indicated!')
            for num in nums:
                sum += num 
            return sum
        else:
            print('There is no start indicated!')
            for num in nums[:end + 1:]:
                sum += num 
            return sum
