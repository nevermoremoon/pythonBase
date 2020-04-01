#!/usr/bin/python
#-*-coding:UTF-8-*-
from __future__ import print_function
import logging
import logging.config
import os
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s :  %(levelname)s : %(message)s',
#     filename="app.log"
# )
# configfile= os.path.abspath(r'..') + '/conf/logging.cnf'
# print(configfile)
logging.config.fileConfig('logging.cnf')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')

