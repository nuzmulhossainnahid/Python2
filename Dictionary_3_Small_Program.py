"""
# This program counts the frequency of characters on a string.
import pprint as pp
text = 'this is a simple text to TEST the code'

letters = {}

for i in text:
    letters.setdefault(i, 0)
    letters[i] = letters[i]+1

pp.pprint(letters)

# This program simulates a password protected app access

password_bank = {'sam': 1234, 'Nahid': 124}
matched = False
x = 0

print('Enter Your Name: ')

while x < 5:
    name = input()
    if name in password_bank:
        for i in range(0,3):
            print('Enter Your Password: ')
            password = input()
            if int(password) in password_bank.values():
                matched = True
                print('Access Granted')
                break
            else:
                print('Wrong Password. Enter again: '+'You have '+str(2-i)+' tries left')
    else:
        print('Thier is no name.Try again')

    x = x+1

    if matched:
        break


# Simulates a phon book
contac_no = {'sam': 000, 'smit': 111}
x = 0
while x < 5:
    print('Enter Your Name(Press Enter to Exit: ')
    name = input()

    if name == '':
        break

    if name in contac_no:
        print('The cantact number of '+name+ 'is '+str(contac_no[name]))
    else:
        print('There is no name .Do add?')
        desc = input()

        if desc == 'yes':
            print('Enter the name: ')
            num = input()
            contac_no[name] = num
            print('Dictionary updated.')
        elif desc == 'no':
            print('Do you quit')
            desc = input()
            if desc == 'yes':
                break
            else:
                print('Keep searching')
        x = x+1

"""

