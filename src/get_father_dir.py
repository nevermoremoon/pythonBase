#!/usr/bin/python
#-*-coding:UTF-8-*-
from __future__ import print_function


import os


print("current dir is : ", os.getcwd() )
path = os.path.abspath(__file__)
print("full path of current file :", path)
print("parent dir of current file :",
      os.path.abspath(os.path.join(os.path.dirname(path), os.path.pardir)))