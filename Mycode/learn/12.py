#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
'''
import subprocess

cmd = subprocess.Popen('ifconfig',stdout=subprocess.PIPE)

print(cmd)
'''

import logging
import time


logger = logging.getLogger('Log')   #日志的实例对象
logger.setLevel(logging.INFO)           #全局

ch = logging.StreamHandler()           #打印到屏幕
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler('access.log')
fh.setLevel(logging.INFO)


# 创建一个handler，用于写入日志文件
# 再创建一个handler，用于输出到控制台

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

logger.addHandler(fh)
logger.addHandler(ch)

