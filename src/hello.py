# This file is a simple Python program which prints several messages greeting the user.

import getpass


def hello(name):
    print("hello " + name + "!")

if __name__ == '__main__':
    # call the function with an argument
    hello("gertrude")
    
    # second test
    hello("fred")
    
    # third test
    hello(getpass.getuser())