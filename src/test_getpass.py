#!/usr/bin/python
#-*-coding:UTF-8-*-

from __future__ import print_function
import getpass


def get_userinput():
    user = getpass.getuser()
    passwd = getpass.getpass('your password')
    return user, passwd

if __name__ == '__main__':
    # print(type(get_userinput()))  return tuple
    print(get_userinput())