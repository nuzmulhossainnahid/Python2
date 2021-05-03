"""

# Open A File
f = open('a.txt', 'w')

print('name = ', f.name)
print('is it closed', f.closed)
print('mode = ', f.mode)
f.write('Nahid')
f.close()


#appending
f = open('a.txt', 'a')
f.write('Nazmul')
f.close()


f = open('a.txt', 'r+')
info = f.read()
print(info)
f.close()

f = open('a.txt', 'w')
f.write('gjfdfdjgf')
f.close()




"""