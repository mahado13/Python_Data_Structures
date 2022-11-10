'''
Author: Mahad Osman
Date: Nov 8th
'''
def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    for hobbyA in a[2]:
        print(hobbyA)
        for hobbyB in b[2]:
            print(hobbyB)
            if ( hobbyA == hobbyB):
                return True
    else: 
        return False
        