#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''


# 经典类 class A:
# 新式类 class A(object)


class A(object):
    n = 'A'

    def f2(self):
        print(' F2 From A')


class B(A):
    n = 'B'

    def f1(self):
        print('From B')

    def f2(self):
        print(' F2 From B')


class C(A):
    n = 'C'

    def f2(self):
        print('From C')


# B--->C--->A      广度优先   同级别 从左到右 没有 再往上找             新式类
# B--->A———>C      深度优先   不合理                                经典类


# 3.0后 不论新式类 还是经典类 都是广度优先
class D(B, C):
    '''
    Test class
    '''

    def __str__(self):
        return 'Dasdfasdf'

d = D()

d.f1()
d.f2()
print(d)


#class 是通通type创建的如下 () {}
MyShinyClass = type('MyShinyClass',(),{'test':123})
a = MyShinyClass()