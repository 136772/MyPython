#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

import time


def consumer(name):
    print('要吃包子啦')

    while True:
        baozi = yield

        print('包子{}来啦，让{}吃了'.format(baozi, name))

def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')

    c1.__next__()
    c2.__next__()
    print('老子要做包子啦')

    for i in range(10):
        time.sleep(1)
        print('{} 做了两个包子'.format(name))
        c1.send(i+1)
        c2.send(i+1)

producer('JaNG')
