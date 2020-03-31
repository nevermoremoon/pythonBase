#!/usr/bin/python
#-*-coding:UTF-8-*-
from __future__ import print_function
import os
import sys


def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise SystemExit(filename + ' does not exists.')
    elif not os.access(filename, os.R_OK):
        #raise get error
        raise SystemExit(filename + ' is not accessiable')
    else:
        print(filename + ' is accessiable')

if __name__ == '__main__':
    main()

