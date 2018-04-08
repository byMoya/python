#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Chain(object):
    def __init__(self, path=''):
        self.__path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self.__path, path))
    def __str__(self):
        return self.__path
    __repr__ = __str__

    def __call__(self):
        print('Chain is called')

s = Chain().status.user.timeline.list
print(s)
print(s())
print(callable(s))