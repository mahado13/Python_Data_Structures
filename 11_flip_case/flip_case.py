'''
Author Mahad
Date: Nov 8th
'''
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newPhrase = ''
    for char in  phrase:
       print(char)
       if (char == to_swap):
           print('They match')
           if(char == char.upper()):
               newPhrase += char.lower()
           else:
               newPhrase += char.upper()
       else:
           newPhrase += char

    return newPhrase



