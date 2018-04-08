#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import types

# 面向对象编程
# 私有变量添加'__'前缀

class Student(object):
    count = 0
    __slots__ = ('__age', '__name', '__score')
    def __init__(self, name, score, age):
        self.__name = name
        self.__score = score
        self.__age = age
        Student.count += 1
    def print_score(self):
        print('%s的%s' % (self.__name, self.__score))
    @property
    def age(self):
        print('property __age get')
        return self.__age
    @age.setter
    def age(self, val):
        print('property __age set', val)
        self.__age = val



wjh = Student('wjh','fuck 90',3)
ccy = Student('ccy','fuck 99',13)
# wjh.__score = '1000'
# wjh.__score
print(wjh.age)
wjh.age = 111
wjh.print_score()
ccy.print_score()
print('Student人数为', Student.count)

# 继承和多肽
class Animal(object):
    def run(self):
        print('Animal is run ...')
a = Animal()
a.run()

class Dog(Animal):
    def run(self):
        print('Dog is run ...')
    def say(self):
        print('wangwang')

class Cat(Animal):
    def run(self):
        print('Cat is run ...')
    def say(self):
        print('miaomiao')

dog = Dog()
dog.run()
dog.say()

cat = Cat()
cat.run()
cat.say()

# 类型判断
print(isinstance(dog,Dog))
print(isinstance(cat,Dog))
print(isinstance(cat,Animal))

# dir获取对象的所有属性
strChar = 'ABC'
print(dir(strChar))

# 改变对象的属性 getattr() setattr() hasattr()
obj = {
    'name':'obj',
    'x':1,
    'y':2
}
getattr(obj, 'year', 404)
