#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

'''
def find_num(base_num,input_num):
    mid = int(len(base_num)/2)
    if len(base_num) >= 1:
        if base_num[mid]>input_num:
            print('number in left',base_num[:mid])
            return find_num(base_num[:mid], input_num)
        elif base_num[mid]<input_num:
            print('number in left')
            return find_num(base_num[mid:],input_num)
        else:
            print('Found find num:',base_num[mid])
    else:
        print('Not Find num')


if __name__ == '__main__':

    list_base = list(range(1,60000,3))
    find_num(list_base,1)


a = []
for i in range(10):a.append(i)

a = [i for i in range(10)]

'''
'''二维数组

[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]

'''
data = [[col for col in range(4)] for row in range(4)]
'''旋转90度'''
for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):

        temp = data[c_index][r_index]
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = temp

        print('-------------')
    for i in data:
        print(i)