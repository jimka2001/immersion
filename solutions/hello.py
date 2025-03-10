# This file is a simple Python program which prints several messages greeting the user.

def hello(name):
    return "Hello, " + name + "!"

def hello_pierre():
    # add a line which calls the `hello` function with the argument "pierre".
    # Careful, the function `hello_pierre` and the function `hello` do not print
    # anything.
    # CHALLENGE: student must complete the implementation.
    return hello("pierre")


if __name__ == '__main__':
    # call the function with an argument
    print(hello("gertrude"))
    
    # second test
    print(hello("fred"))

    # following the two examples above, add a line so that python will print hello to pierre.
    # CHALLENGE: student must complete the implementation.
    print(hello_pierre())
