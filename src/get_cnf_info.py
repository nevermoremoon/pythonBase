#!/usr/bin/python
#-*-coding:UTF-8-*-
from __future__ import print_function
import ConfigParser
import shutil
import os


def get_mysql_info(sec, cnfname):
    cf = ConfigParser.ConfigParser(allow_no_value=True)
    cf.read(cnfname)
    print(cf.sections())
    server_info = cf.options(sec)
    print(server_info)
    print(cf.items(sec))
    # print(cf.get(sec, 'datadir'))

def write_mysql_info(cnf, cnfname):
    cf = ConfigParser.ConfigParser(allow_no_value=True)
    bakname = cnfname + '.bak'
    if os.path.exists(bakname):
        os.remove(bakname)
        shutil.copyfile(cnfname, bakname)
    else:
        shutil.copyfile(cnfname, bakname)

    cf.add_section(cnf)
    cf.set(cnf, 'host', '127.0.0.1')
    cf.set(cnf, 'port', '3307')
    cf.write(open(bakname, 'w'))
    return get_mysql_info(cnf, bakname)


if __name__ == '__main__':
    write_mysql_info('xxxx', '/mnt/conf/my.ini')