print('How many cats do you have?')
numCats = input()
try:  # Imput validation
    if int(numCats) >= 4:  # Expecting an integer
        print('Thats is a lot of cats!')
    elif int(numCats) <= -1:
        print('No negative numbers!')
    else:
        print('Thats not that many!')
except ValueError:
    print('You did not enter a number.')
