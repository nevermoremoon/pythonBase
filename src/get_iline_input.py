#!/usr/bin/python
#-*-coding:UTF-8-*-

from __future__ import print_function
import sys
import fileinput


def get_content():
    return sys.stdin.readlines()

# print(get_content())

for line in fileinput.input():
    meta = [fileinput.filename(), fileinput.fileno(), fileinput.filelineno(), \
            fileinput.isfirstline(), fileinput.isstdin()]
    print(*meta, end="")
    print(line, end="")