#!/usr/bin/env python

import os

# from the current directory get the list of files ending with .py
filenames = [x for x in os.listdir('.') if x.endswith('.py')]

# Rename file from e_*.py to demo_.py
for f in filenames:
    os.rename(f, f.replace('e_', 'demo_'))
