#!/usr/bin/env python

""" Demo logging."""

import logging

LOG_FILE = './output/test.log'

# Get a logger class linked to an id/name
logger = logging.getLogger('MyApp')

# Define a formatter for the messages
formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')

# Create handler for streaming the log.
# You can have more than one.

handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

handler_file = logging.StreamHandler(open(LOG_FILE, 'w'))
handler_file.setFormatter(formatter)
logger.addHandler(handler_file)

# Set minimum level logging
logger.setLevel(logging.DEBUG)

# This is how to log stuff
logger.info('this is an info message')
logger.debug('this is a debug message')
logger.warning('this is a warning message')
logger.error('this is an error message')
logger.critical('this is a critical message')
