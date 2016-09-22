#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

# def show(*args,**kwargs):
#     print(args,type(args))
#     print(kwargs,type(kwargs))
#
# l = [11,22,33,44]
# d = {'k1':'v1','k2':'v2'}
#
# show(*l,**d)

# s1 = '{} is {}'
# l = ['alex','sb']
# result = s1.format(*l)   #如果传入列表那么就要制定为 * 的参数
#
# print(result)
#
# s2 = '{name} is {acter}'       #指定key
# d = {'name':'alex','acter':'2b'}
# result = s2.format(**d)        #如果传入字典那么就要制定为 ** 的参数
#
# print(result)



# lambda===========================如果要写简单的函数 可以使用它
#
# def a(i):
#     i += 1
#     return i

# a = lambda i: i+1    #i 为行参， 可多个 然后加：
# #  创建形式参数i
# # 函数内容， a+1 并把结果return
#
# print(a(99))

# class Foo:
#     def __repr__(self):
#         return 'bbbbbb'
#
# f = Foo()
# ret = ascii(f)
# print(f)
# print(ret)

l1 = [11,22,33,44]
# new_li = map(lambda x: x+100,l1)
# for i in new_li:
#     print(i)
# l = list(new_li)
# print(l)
#
# def a(num):
#     return num+100
#
# new_li = map(a,l1)
# print(new_li)

#
# def func(x):
#     if x>33:
#         return True
#     else:
#         return False
#
# # n = filter(func,l1)
# n = filter(lambda x:x>33,l1)
# print(list(n))


f = open('test.log','r+')
'''
f.tell() #查看当前指针
f.read()
# print(f.tell())
f.seek(1) #设置当前指针位置

f.close()
'''

f.seek(5)
# print(f.read())
f.truncate()
f.close()