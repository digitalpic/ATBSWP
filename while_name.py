# Input validation while loop is True
name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thanks')
