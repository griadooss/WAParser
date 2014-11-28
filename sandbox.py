#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys # Import the sys module
import csv # Import the csv module
import constants as c # Import the project specific constants.py file
from csvvalidator import *

s = 'this is a string'
s1 = 'th@is i*s ,a!ls)o a*(& str~,,./ing'

def fun(s):
    l =[]
    for a in s:
        if a.isalpha():
            l.append(a)
        else:
            if a == ' ':
                l.append(a)
    return ''.join(l)

print s
print s1
print fun(s1)

            
        