#!/usr/bin/env python

""" Demo-ing argparse. """

import argparse
parser = argparse.ArgumentParser(description='This is a sample program')
parser.add_argument("user", help="user")
parser.add_argument("age", help="age for the user", type=int)
parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
args = parser.parse_args()
print('User {}, Age {}'.format(args.user, args.age))
if args.verbose:
    print('Running in verbose mode')


##################################################################################################
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("language")
    parser.add_argument("name")

    args = parser.parse_args()


    if(args.language == "Python"):
        print("Yes, that is a great choice")
    else:
        print("Have you tried python")

    print(f'Hello {args.name}, this was a simple introduction to argparse module')

"""try running below
    python commandlinearguments.py Python David

    python commandlinearguments.py Java Lisa

    python commandlinearguments.py -h

"""