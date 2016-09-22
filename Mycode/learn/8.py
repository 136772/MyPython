#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

import re

'''
phone_str = "hey my name is alex, and my phone number is 13651054607, please call me if you are pretty!"
phone_str2 = "hey my name is alex, and my phone number is 18651054604, please call me if you are pretty!"

pattern = re.compile('(1)([34578]\d{9})')
m = re.search(pattern,phone_str)
print(m.group())


ip_addr = "inet 192.168.60.223 netmask 0xffffff00 broadcast 192.168.60.255"

pattern = re.compile('(\d{1,3}\.){3}\d{1,3}')
m = re.search(pattern,ip_addr)

contactInfo = 'Oldboy School, Beijing Changping Shahe: 010-8343245'
match = re.search(r'(?P<last>\w+),(?P<first>\w+):(?P<phone>\S+)', contactInfo) #分组)
print(match.group('last'))
'''

data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
print(data)

for i in range(1,len(data)):
    temp = 0
    for j in range(len(data)-i):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
    print(data)