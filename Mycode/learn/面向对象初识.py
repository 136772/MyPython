#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

'''
封装 多态 继承
'''
'''封装    self 就是实力本身 比如 p1就是实例
class Role(object):
    ac = None   #存在类的内存对象 ,类属性，公共
    members = 0   #类变量  属性
    # __init__初始化方法
    def __init__(self, name, role, weapon, live_value): #真正实例化之后存在 t1,p1内存对象中 ，成员变量，私有  self  实例本身
        self.name = name     #实例变量， 属性
        self.role = role
        self.weapon = weapon
        self.live_value = live_value
        Role.members += 1                                #每生成一个实例的计数

    def buy_weapon(self, weapon):                        #存在Role内存对象 和实例化没有关系，公共，省内存空间  叫类的方法
        self.weapon = weapon
        print('{} is buying [{}]'.format(self.name,self.weapon))

        print(self.ac)

p1 = Role('Sanjiang','Police','B10',90)
t1 = Role('ChunYun','terrorist','B11',100)
t2 = Role('t2','Police','B10',90)
t3 = Role('t3','terrorist','B11',100)

p1.buy_weapon('AK47')
t1.buy_weapon('B51')

p1.ac = 'China Brand'   #这样不去访问 Role.ac 而是创建了一个p1的ac
t1.ac = 'US Brand'

Role.ac = 'Japanese Brand'
Role.weapon = 'XFX' #类的内存中创建了一个XFX

print(p1.weapon,p1.ac)
print(t1.weapon,t1.ac)
print(t2.weapon,t2.ac)
print(t3.weapon,t3.ac)

print(Role.members)
'''
'''类的方法'''