#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author:JaNG
@email:136772@163.com
'''
'''
class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo = '可口可乐'
    def drivk(self):
        print('Energy')
coke = CocaCola()
print(coke.drivk())


class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self):
        for element in self.formula:
            print('Cok has {}'.format(element))

    def drink(self):
        print('Energy!')

coke = CocaCola()



class CocaCola():
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine',
    ]

    def __init__(self, logo_name):
        self.logo_name = logo_name

    def drink(self):
        print('You got {} cal energy! caffeine={}'.format(self.calories,self.caffeine))

class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]

coke = CocaCola('普通可乐')
coke.drink()
coke_a = CaffeineFree('Cocacola-Free')
coke_a.drink()


class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42

obj_a = TestA()
print(TestA.__doc__)
print(obj_a.__doc__)

print(TestA.attr)
print(obj_a.attr)

fn = ('张','王','李','刘')
ln1 = ('娉','览','莱','屹')
ln2 = ('治明','正顺','书铎')

import random
class FakeUser:
    def fake_name(self,amount = 1,one_word = False,two_word = False):
        n=0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn)+random.choice(ln1)
            elif two_word:
                full_name = random.choice(fn)+random.choice(ln2)
            else:
                full_name = random.choice(fn)+random.choice(ln1+ln2)

            yield full_name
            n+=1
    def fake_gender(self,amount = 1):
        n = 0
        while n <= amount:
            gender = random.choice(('男','女','未知'))
            yield gender
            n+=1


class SnsUser(FakeUser):
    def get_followers(self,amount =1,few = True, a_lot = False):
        n = 0
        while n<= amount:
            if few:
                followers = random.randrange(1,50)
            elif a_lot:
                followers = random.randrange(200,10000)
            yield followers
            n+=1

user_a = FakeUser()
user_b = SnsUser()

for name in user_a.fake_name(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)

import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    client.send(b"Hello, Seven")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
'''
import re
string = 'asd \n jdc \n ews'
m = re.search('\W+',string)
print(m.group())