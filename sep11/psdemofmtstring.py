"""demo for the formatted string"""


name, age = 'sarah willams', 3   # unpacking aka parallel assignment


print('I am name, age years old')
print(f'I am {name}, {age} years old')
print(f'I am {name}, {age*3} years old')
print(f'I am {name.title()}, {age*3} years old')
print(f'I am {name.capitalize()}, {age*3} years old')
print()

print('I am {}, {} years old'.format(name.title(), age * 3))  #

