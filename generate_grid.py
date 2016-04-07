#!/usr/bin/python
import random
import sys
from get_int import *
rows = get_int('rows:',1,None)
columns = get_int('columns:',1,None)
minimum = get_int('minimum:',-10000000,0)


default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int('maximum(or Enter for' + str(default) + '):',minimum,default)
for each in range(rows):
    line = ''
    for every in range(columns):
        i = random.randint(minimum,maximum)
        s = str(i)
        s = ' ' + s
        line += s
    print(line)
