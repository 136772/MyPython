#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
'''
def login(func):
    def inner(*args,**kwargs):
        print('Login')
        return func(*args,**kwargs)
    return inner

@login
def home(name):
    print('welcom {}'.format(name))


home('JanG')



def login(name,psword):
    print('this is login')

def errorh(name,psword):
    print('this is errorh')

def ha(func1,func2):
    def wapper(mainf1):
        def inner(name,psword):
            login = func1(name,psword)
            mainf = mainf1(name,psword)
            errorh = func2(name,psword)
        return inner(name,psword)
    return wapper

@ha(login,errorh)
def index(name,pasword):
    print('index{}  {}'.format(name,pasword))

index('jang',123)
'''
def login(func):
    def inner(*args,**kwargs):
        print("123123")

        return func (*args,**kwargs)
    return inner

@login
def say_hi():
    print('456456456')

say_hi()