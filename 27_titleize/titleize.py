'''
Author: Mahad Osman
Date: Nov 9
'''
def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    oldList = phrase.lower().split(' ')
    newList = []
    for title in oldList:
        newList.append(title.capitalize())
        #','.join(newList)
    return(' '.join(newList))