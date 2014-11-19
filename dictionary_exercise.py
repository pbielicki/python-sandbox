from datetime import date

def find_by_phone(contacts, phone_number):
    result = []
    for contact in contacts:
        phone = contacts[contact][0]
        if phone == phone_number:
            result.append(contacts[contact])

    return result

def build_phone_index(contacts):
    result = {}
    for contact in contacts:
        phone = contacts[contact][0]
        #if phone is None:
        #    continue
        
        if phone in result:
            v = result.get(phone)
        else:
            v = []
            result[phone] = v

        #v = result.setdefault(phone, [])
        v.append(contact)
        
    return result

contacts = dict()
contacts[1] = (123456, 'address', date(1980, 11, 20))
contacts[2] = (333456, 'address', date(1981, 1, 2))
contacts[3] = (223456, 'address', date(1989, 2, 11))
contacts[4] = (663456, 'address', date(1983, 6, 30))
contacts[5] = (123456, 'address 123', date(1981, 3, 15))
contacts[6] = (883456, 'address', date(1983, 7, 1))
contacts[7] = (993456, 'address', date(1988, 9, 2))
contacts[8] = (883456, 'address', date(1983, 10, 9))
contacts[9] = (None, 'address', date(1983, 10, 9))

print find_by_phone(contacts, 123456)
index = build_phone_index(contacts)
print index
print index[None]