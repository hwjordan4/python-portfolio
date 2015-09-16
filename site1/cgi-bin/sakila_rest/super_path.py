__author__ = 'Ben'

# add the super directory to sys.path

import sys
from os.path import split
sys.path.insert(0,split(split(__file__)[0])[0])
