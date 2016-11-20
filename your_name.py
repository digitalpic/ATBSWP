
# This program asks for your name and age
print("Hi there, stranger - what's your name?\n")  # Calling the print function
myName = input()
print("It's good to meet you" + myName)
print('The length of your name is:')
print(len(myName))  # Len takes string argument and evaluates to the length

# Age
print("What's your age")
myAge = input()
print('Your age is ' + myAge)

# Return string and integer values and converts the data types. Use
# float() value for decimals
print('You will be ' + str(int(myAge) + 1) + ' sometime soon')
