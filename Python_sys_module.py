# Python sys module
# The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions.


# import sys

# First, we have to import the sys module in our program before running any functions.

# sys.modules
# his function provides the name of the existing python modules which have been imported.

# sys.argv

# This function returns a list of command line arguments passed to a Python script. The name of the script is always the item at index 0, and the rest of the arguments are stored at subsequent indices.

# sys.base_exec_prefix

# This function provides an efficient way to the same value as exec_prefix. If not running a virtual environment, the value will remain the same.

# sys.base_prefix

# It is set up during Python startup, before site.py is run, to the same value as prefix.

# sys.byteorder


# It is an indication of the native byteorder that provides an efficient way to do something.


# sys.maxsize

# This function returns the largest integer of a variable.

# sys.path

# This function shows the PYTHONPATH set in the current system. It is an environment variable that is a search path for all the python modules.


# sys.stdin

# It is an object that contains the original values of stdin at the start of the program and used during finalization. It can restore the files.


# sys.exit

# This function is used to exit from either the Python console or command prompt, and also used to exit from the program in case of an exception.

# sys.getrefcount

# This function returns the reference count of an object.


# sys executable

# The value of this function is the absolute path to a Python interpreter. It is useful for knowing where python is installed on someone else machine.


# sys.platform

# This value of this function is used to identify the platform on which we are working.

