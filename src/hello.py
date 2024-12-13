# This file is a simple Python program which prints several messages greeting the user.

import getpass


def hello(name):
    print("hello " + name + "!")

if __name__ == '__main__':
    # call the function with an argument
    hello("gertrude")
    
    # second tests
    hello("fred")
    
    # third tests
    hello(getpass.getuser())
