'''
you manages your contacts in Python


contacts is a dictionary with an ID of your contacts as keys, and a tuple
(phone_number, address, birthday) as values (any of these can be None
if unknown)

'''


def find_by_phone(contacts, phone_number):
    '''returns a list of contact IDs with the given phone number'''
    matches = []
    for id in contacts:
        phone, _addr, _birthday = contacts[id]
        if phone == phone_number:
            matches.append(id)
    return matches

def build_phone_index(contacts):
    """return a dictionary with phone numbers as keys and list of contact
    IDs as values.

    unknown phone numbers are not included"""
    index = {}
    for id in contacts:
        phone, _addr, _birthday = contacts[id]
        if phone is None:
            continue
##        # one way
##        ids = index.get(phone, [])
##        ids.append(id)
##        index[phone] = ids
##        # another one:
##        ids = index.setdefault(phone, [])
##        ids.append(id)
        # simple, a bit more efficient if lots iof appending
        if phone not in index:
            ids = []
            index[phone] = ids
        else:
            ids = index[phone]
        ids.append(id)
        
    return index


contacts = {'joe':('23423454534', None, None),
            'jack': ('23423454534', None, None),
            'william': ('23423454534', None, None),
            'averell': (None, None, None),
            }

print find_by_phone(contacts, '23423454534')
print find_by_phone(contacts, '23423454535')
print build_phone_index(contacts)


