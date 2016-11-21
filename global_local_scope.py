spam = 42  # global variable


def spam():
    eggs = 'Hello'  # assignment statement is local variable
    bacon()
    print(eggs)


def bacon():
    global eggs  # Global statement
    eggs = 9
    ham = 12

    print(eggs)

eggs = 42
spam()
print(eggs)
