#!/usr/bin/env python

"""Demoing os environment variables passing."""

import os
if "VAR1" in os.environ.keys():
    print('Passed env variable {} = {}'.format("VAR1", os.environ["VAR1"]))
else:
    print('You need to call this script as VAR1=Hello python e_osenvironment.py')
