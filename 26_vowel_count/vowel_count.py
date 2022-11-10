'''
Author: Mahad Osman
Date: Nov 9th
'''
def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowelLocker = {}
    for char in phrase:
        #print(char)
        if(char.lower() in 'aeiou'):
          #  print('it is a vowel')
            if(char.lower() in vowelLocker.keys()):
                vowelLocker[char.lower()] += 1
            else:
                vowelLocker[char.lower()] = 1
    return vowelLocker
