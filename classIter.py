#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代一个类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 实例本身就是迭代对象 返回自己
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        print('a = %s' % self.a)
        # 退出循环的条件
        if self.a > 100:
            raise StopIteration()
        # 返回下一个值
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
for n in Fib():
    print(n)
f = Fib()
print('f[5] %s' % f[5])