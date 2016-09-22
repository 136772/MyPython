#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
'''
name = iter(['jang','rourou','book'])
print(name.__next__())
print(name.__next__())
print(name.__next__())
'''

def cash_money(amount):
    while amount>0:
        amount -= 1
        yield '取了{}，还剩{}'.format(1,amount)


temp = cash_money(5)
for i in temp:
    print(i)