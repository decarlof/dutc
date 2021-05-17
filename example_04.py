# QUESTION: what is the difference between
#           `sys.version` and `sys.version_info`?

import sys
import math
from math import atan, atan2

from sys import version
from sys import version_info

# print(f'{version      = }')
# print(f'{version_info = }')

# print(dir(version))
# print(dir(math.atan))
help(atan)
help(atan2)