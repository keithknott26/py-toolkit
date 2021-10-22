# You'll typically need to import one or more modules to have the script funtionality you want.

# Import a single module (library)
import arcpy

# Import multiple modules (libraries)
import arcpy, os, sys, datetime, traceback

# Import a specific function from a module, and give a nickname to the function
from os import path as p
# You just imported the "path" function from the "os" module. 
# You can call the "path" function with its nickname, "p".

# What modules do I need and what do they do?
# Refer to the list below and feel free to add more.

import arcpy # Gets functionality of standard ArcGIS toolboxes. 
# However, this does NOT automatically give you access to Spatial Analyst functions. 
# For full access to all ArcGIS functionality including Spatial Analyst, use the following snippet:
import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")

import os # Miscellaneous operating system interfaces
# Provides access to operating system functionality such as file and directory paths.
# See https://docs.python.org/2/library/os.html

import sys # System-specific parameters and functions
# See https://docs.python.org/2/library/sys.html

import datetime # Basic date and time types
# Can be used for time-stamping.
# See https://docs.python.org/2/library/datetime.html

import time # Time access and conversions
# Can be used for time-stamping.
# See https://docs.python.org/2/library/time.html

import traceback # Print or retrieve a stack traceback
# Used for error handling.
# See https://docs.python.org/2/library/traceback.html

import Tkinter # Python interface to Tcl/Tk 
# Can be used to get pop-up windows for user input. Not typically needed, but for some situations you may want it.
# See https://docs.python.org/2/library/tkinter.html