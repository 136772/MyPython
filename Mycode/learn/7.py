#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
import re
def multiply_divide(equation):
    pass

def add_subtract(equation):

    if len(equation.split('+'))>1:
        n1,n2 = equation.split('+')
        value = float(n1)+float(n2)

    elif len(equation.split('-'))>1:
        n1, n2 = equation.split('-')
        value = float(n1) - float(n2)
    else:
        print('1')
    return value

def parentheses(equation):
    expression = equation.replace(' ', '')
    patter = '\([^()]+\)'
    m = re.search(patter,expression)
    if m:
        m = m.group()
        before,after = re.split(patter,expression,1)
        m = m.strip('()')
        if ('*' or '/') in m:
            pass
        else:
            add_subtract(m)



if __name__ == '__main__':
    equation = '1-2*(((-60-30+(-40.0-5)*(9/-2*5/3+7/3*-99/4*2998+10*568/14)))-(-4*3)/(16-3*2))'
    parentheses(equation)