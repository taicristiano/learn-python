person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'
    }
person['name'] # Vũ Thanh Tài

person['status'] # single

person['status'] = 'married'
print(person)
#{'name': 'Vu Thanh Tài', 'age': 22, 'male': True, 'status': 'married'}

print(person)
#{'name': 'Vu Thanh Tài', 'age': 22, 'male': True}

person.clear();
print(person)
#{}

#del person
print(person)
#error: name 'person' is not defined

person = {
    'name': 'Vũ Thanh Tài',
    'option': {
            'age': 22,
            'male': True,
            'status': 'alone'
        }
    }

print(person['option']['age'])
# 22