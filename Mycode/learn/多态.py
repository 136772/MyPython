#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

'''多态'''
class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        raise NotImplementedError('')


class Cat(Animal):
    def talk(self):
        return 'Meow'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof'

# animals = [Cat('Missy'),Dog('Lassie')]

def animal_talk(obj):
    print(obj.talk())

c = Cat('Sanjiangmei')
d = Dog('Sanjiangyuan')

animal_talk(c)
animal_talk(d)

# for animal in animals:
#     print(animal.name , animal.talk())