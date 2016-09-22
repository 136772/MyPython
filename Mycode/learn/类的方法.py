#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

class Animal:
    def __init__(self,name):
        self.name = name

    hobbie = 'meat'

    @classmethod     #类方法 只能通过 Animal.talk()不能访问实例变量
    def talk(self):
        print('{} is talking ...'.format(self.hobbie))

    @staticmethod     #静态方法 不能访问类变量 和实例变量！！
    def walk():
        print('is wolking ...')

    @property      #属性    把方法改为属性 不用（）就可以调用
    def habit(self):
        print("{} habit is XXOO".format(self.name))

    @habit.setter    #如果特别想给 habit 赋值 可以这么用
    def habit(self, num):
        self.num = num
        print(self.num)

    @habit.deleter    #如果想删除
    def habit(self):
        print('total player got deleted')
        del self.num

#类方法
# Animal.talk()
# d = Animal('sanjiang')
# d.talk()


# d = Animal('Sanjiang')
# d.habit


# property 传值
d = Animal('Sanjiang')

d.habit = 3

print(d.habit)
