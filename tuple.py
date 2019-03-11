day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
a = (10,)

day = ('monday', 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')
day[0] # monday

day[-2] # saturday


print(day[1:3]) # ('tuesday', 'wednesday')

day[:3] # ('monday', 'tuesday', 'wednesday')

day[1:] # ('tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday')

del day

#print(day) # Error: name 'day' is not defined

day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday')

day = day1 + day2

print(day)

day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)

# day = day1 + day2

print(day2)
# ('thursday', 'friday', 'saturday', 'sunday', ('monday', 'tuesday', 'wednesday'))

print(day2[4][0]) # monday