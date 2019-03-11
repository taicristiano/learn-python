name = ['VU Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name[0]) # Vu Thanh Tai
print(name[1]) # Nguyen Van A
print(name[2]) # Nguyen Thi E
# or
print(name[-3]) # Vu Thanh Tai
print(name[-2]) # Nguyen Van A
print(name[-1]) # Nguyen Thi E


print(name[0:2])
# ['Vu Thanh Tai', 'Nguyen Van A']

# or

print(name[-3:-1])
# ['Vu Thanh Tai', 'Nguyen Van A']


name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

name[1] = 1996
print(name)
# ['Vu Thanh Tai', 1996, 'Nguyen Thi E']

name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E']

del name[2]
print(name)
# ['Vu Thanh Tai', 'Nguyen Van A']


option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

subList = myList[1] # [12, 5, 1996]
subList[0] # 12

myList[1][0] # 12
print(myList[1][0])