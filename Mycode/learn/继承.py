#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''

'''继承'''


class SchoolMember(object):
    member_nums = 0
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

        self.enroll()

    def enroll(self):

        SchoolMember.member_nums += 1          #注意不是Self ！！！！！
        print('The {} SchoolMember {} is enrolled!'.format(self.member_nums,self.name))   #实例中没有更改member_num所以可以调用类

    def tell(self):
        print('Hello My name is {}'.format(self.name))


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, course, salary):
        super(Teacher, self).__init__(name, age, sex)  # 把父类的 name age sex 继承过来
        # SchoolMember.__init__(self,name,age,sex) #老写法
        self.course = course
        self.salary = salary

    def teaching(self):
        print('Tearcher {} is teaching {}'.format(self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, course, tuition):
        super(Student, self).__init__(name, age, sex)
        self.course = course
        self.tuition = tuition

    def pay_tuition(self):
        print('ca, student {} paying tution {}'.format(self.name, self.tuition))


t1 = Teacher('alex', 22, 'F', 'PY', 1000)
t2 = Teacher('Tenglan', 25, 'N/A', 'PY', 900)

s1 = Student('SanJiang', 24, 'Female', 'Python', 150000)
s2 = Student('BaoAn', 26, 'Female', 'Python', 140000)

