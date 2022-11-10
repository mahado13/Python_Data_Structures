'''
Author: Mahad
Date: Nov 8th
'''
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    mutipleLetters = {}
    for char in phrase:
        #if it doesnt'exist we set it to 1 and if it does we increment it
        mutipleLetters[char] = mutipleLetters.get(char, 0) + 1
    return mutipleLetters
    #     if(mutipleLetters.get(char) != None):
    #         mutipleLetters.get(char,1)
    #     else:#(mutipleLetters.get(char)):
    #         mutipleLetters[char] += 1
    # return mutipleLetters
