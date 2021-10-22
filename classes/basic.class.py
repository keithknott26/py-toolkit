
class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def hello(name, loud=False):  # loud is optional
        if loud:
            print('HELLO, %s' % name.upper())
        else:
            print('Hello, %s!' % name)

g = Greeter('Fred')
g.hello()
g.hello(loud=True)


################################################################

from itertools import compress, cycle
from functools import reduce
import string

class Functional:
    def get_even_letters():
        """
        get the even letters using `compress` and `cycle`. 
        """
        letters = string.ascii_uppercase
        even_letters = compress(letters, cycle([0,1]))
        print(list(even_letters))


f=Functional
f.get_even_letters()
