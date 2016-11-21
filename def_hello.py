def hello(name):  # def statement defines a function and  pass an argument to parameter
    print('Howdy! ' + name)

# Call the hello function
hello('Alice')
hello('Bob')
hello('Alice')


def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)
