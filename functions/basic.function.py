
def hello(name, loud=False):  # loud is optional
    if loud:
        print('HELLO, %s' % name.upper())
    else:
        print('Hello, %s!' % name)

hello('Bob')  # "Hello, Bob"
hello('Fred', loud=True)  # "HELLO, FRED"