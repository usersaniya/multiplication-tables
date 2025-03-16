import imported_file
imported_file.func1()
imported_file.input_value()

import imported_file as imp
imp.func1()

from imported_file import input_value
result= input_value()

from imported_file import input_value as we
op=we()
import imported_file
print(dir(imported_file))

import math
print(dir(math))
print(math.fabs, type(math.fabs))