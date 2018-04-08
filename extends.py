#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承

# 基类
class Animal(object):
    pass

# 各大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('Running ...')
class Flyable(object):
    def fly(self):
        print('Flying ...')

# 各种具体类
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Runnable):
    pass
class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Flyable):
    pass

dog1 = Dog()
parrot1 = Parrot()

dog1.run()
parrot1.fly()
