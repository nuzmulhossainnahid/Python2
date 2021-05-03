identity = {'Name': 'Nahid', 'Age': '22','job': 'Student'}
"""
for i in identity.values():
    print(i)
for i in identity.values():
    print(i)
for i in identity.items():
    print(i)
x = list(identity.keys())
y = list(identity.values())

print(x)
print(y)
for k, v in identity.items():
    print('key: '+k+' value: '+v)


# print('Name' in identity)
# print('fgf' in identity)

# print("Nahid" in identity.values())

print(str(identity.get('Name', 'DEFULT')))
print(str(identity.get('Height', 'DEFULT')))

# Add value
print(identity.setdefault('Name', 'cosmos'))
print(identity.setdefault('Height', '6.1'))
print(identity)

"""