import math #import module
a = 3.2
print(math.ceil(a)) # 4
print(math.floor(a)) # 3


from math import ceil #import only
a = 3.2

print(ceil(a))
# result: 4

#print(floor(a))
# result name 'floor' is not defined


import function as helper #import module create
from function import tong as tong #import module create

#import function #import module create
a = tong(5, 6)
#a = helper.tong(5, 6)
print(a)

import os, sys
lib_path = os.path.abspath(os.path.join('modules'))
sys.path.append(lib_path)
# import
from helper import sumNew

print(sumNew(1,4));
