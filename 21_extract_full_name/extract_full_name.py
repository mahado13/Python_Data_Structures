'''
Author: Mahad 
Date: Nov 9th
'''
def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    nameList  = []
    for items in people:
        print(items)
        fullname = ''
        for values in items.values():
            #print(values)
            if(fullname == ''):
                print('adding values')
                fullname += values
            else:
                fullname += ' '+values
                nameList.append(fullname)
        
    return nameList



# %run extract_full_name.py
#  names = [ {'first': 'Ada', 'last': 'Lovelace'},{'first': 'Grace', 'last': 'Hopper'}]
