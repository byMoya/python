#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# 引入数学包
import math
import os
from functools import reduce
import functools
import sys
from enum import Enum, unique

'learning python'

__author__ = 'D'

print(100+200)
print('fuck wjk')

# name = input('请输入:')
# print('fuck',name)

# # python注释
# a = int(input('请输入整数:'))
# if a>10:
# 	print(a,'大于10')
# else:
# 	print(a,'小于等于10')

print('l1\nl2\nl3')

# 布尔运算
True
False
3>2
3>2 and 1>2
3>2 or 1>2
not 1>2

print(10/3)
print(10//3)

print(ord('A'))
print(chr(25991))

# python保存字节
# 使用decode解码 decode('ascii') decode('utf-8')
bBytes = b'fuck'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore')

# 计算字符长度
print(len('AAA计算'),len(b'\xe4\xb8\xad\xe6\x96\x87'),b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('%s fuck %s %d 次' % ('成成','文件红',99))
formatTpl = '{0} fuck {1} {2} 次' 
print(formatTpl.format('成成','文件红',99))
print('%s的成绩从去年的%d分提升到了今年的%s分,提升了%.1f%%' % ('小明',75,85,(85-75)*100/75))

listDef = ['snc','kz','alia']

# Array队尾插入
listDef.append('tx')
# Array任意位置插入
listDef.insert(1,'vip')
# pop默认删除队尾元素或pop(i)
listDef.pop(0)

print(listDef)
print('listDef数组长度为%s' % (len(listDef)))
print(listDef[2])
#获取最后一个元素
print(listDef[-1])

# tuple元组，不可修改的Array
classNames = ('cc','wjk','xx','lds','hp')
print('{0},{1}'.format(classNames,classNames[0]))
tupleOne = ('onePice',)
print('{0},{1}'.format(tupleOne,tupleOne[0]))

age = 10
if age>18:
	print('%s is adult' % (age))
elif age>=6:
	print('%s is teen' % (age))
else:
	print('%s is kid' % (age))


height = 1.8
weight = 80.5
bmi = weight/(height*height)
print(bmi)
if bmi>=32:
	print('严重肥胖')
elif bmi<32 and bmi>=28:
	print('肥胖')
elif bmi<28 and bmi>=25:
	print('过重')
elif bmi<25 and bmi>=18.5:
	print('正常')
else:
	print('过轻')

for name in classNames:
	print(name)

num = 0
for i in range(1000):
	num += i
print('num = %d' % (num))

whileNum = 0
n = 99
while n > 0:
	whileNum += n
	n -= 2
print('while num = %d' % (whileNum))

for i in range(100):
	if i<10:
		print(i)
	else:
		continue

# Python字典dict = Map or Object
d = {'wjh':100,'lxc':95,'zxx':70}
print('test dict %s' % (d['lxc']))
# d['asdasd'] 报错
# 判断key是否存在
print('asdasd' in d)
print(d.get('asdasd'))
d['ccccc'] = 1
print('dict is {0}'.format(d))

# 删除某个键值
d.pop('lxc')
print('lxc is {0}'.format(d.get('lxc')))

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set(['a','b','c'])
s.add(4)
s.add('b')
s.remove('a')
print('set is {0}'.format(s))

# set的交集与并集
s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7,8])
print('交集',s1 & s2)
print('并集',s1 | s2)

# 数据类型转换
# int() float() str() bool()

def cycleArea(r):
	return int(3.14*r*r)
print('cycleArea 圆面积:',cycleArea(6))

# 空函数或空内容pass
def function():
	pass

#对参数类型做校验
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad arguments type')
	if x > o:
		return x
	else:
		return -x
# my_abs('AAA计算')

# 函数返回多个参数
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
# 返回值是一个tuple
	return nx, ny
mx, my = move(100, 100, 60, math.pi/6)
r = move(100, 100, 60, math.pi/6)
print('def move return tuple', mx, my)
print('def move return tuple',r)

def power(x,n=2):
	s = 1
	while n>0:
		n = n - 1
		s = s * x
	return s
print(power(5))
print(power(5,6))

# 指向型默认参数
def add_end(L=None):
	if L is None:
		L = []
	L.append('End')
	return L
print('L arguments default', add_end())

# 可变参数，在参数前面加*,PS:*等于js里的...
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n 
	return sum
print('可变参数求和',calc(1,5,7,9,11))

# 关键字参数使用**, **把字典每个key:value循环出来
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extendParams = {'job':'fucker', 'sing':'let it be', 'city':'GZ', 'do':'drink'}
def person(name,age,**kw):
	p = {
		'name':name,
		'age':age,
		'other':kw
	}
	return p
print('可变参数 **',person('wjh', 10, gender = 'M', job='fucker'))
print('可变参数 **',person('wjh', 10, **extendParams))

testDict = {name:'wjh'}

# 参数组合
def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
f1(1,2)
f1(1,2,None,'mo','la','la',**{
	'name':'fuck',
	'age':'10'
})

def product(*nums):
    sum = 1
    for i in nums:
        sum = sum * i
    return sum
print(product(1,2,3,4,5,6,7,8))

# 递归
def fetch(n):
	if n == 1:
		return n
	else:
		return n * fetch(n-1)
print(fetch(8))

#尾递归
def fetchOpt(n):
	return fetch_iter(n,1)
def fetch_iter(num,sum):
	if num == 1:
		return sum
	else:
		return fetch_iter(num-1,num*sum)
print(fetchOpt(100))

# 切片操作符 [start:end:space]
# 甚至什么都不写，只写[:]就可以原样复制一个list：

Lis = ['Mic','Sar','Qb','Li','Di']
print(Lis[1:3])

ListNums = []
for i in range(1,1000):
	ListNums.append(i)
print(ListNums[100:500:2])

def trim(s):
	start = 0
	end = len(s)
	startStatus = True
	endStatus = True
	for i in range(len(s)):
		if s[start:1] == ' ' and startStatus:
			start += 1
		else:
			startStatus = False
		if s[end:1] == ' ' and endStatus:
			end -= 1
		else:
			endStatus = False
		if startStatus and endStatus:
			break
	return s[start:end]
print('value is',trim(' aa a fuck '))
print('value is',trim(''))

# 迭代
D = {
	'a':1,
	'b':2,
	'c':3
}
DS1 = ''
DS2 = ''
for value in D.values():
	DS1 += str(value) + ' ' 
for k,v in D.items():
	DS2 += k + ':' + str(v) +' '
print(DS1)
print(DS2)

Dlist = ['A','B','C','D','E','F','G','H']
for i,value in enumerate(Dlist):
	print(i,value)

# 查找list里的最大和最小值
def findMinAndMan(L):
	start = len(L) or None
	if not start:
		return start
	max = start
	min = start
	for v in L:
		if v > max:
			max = v
		if v < min:
			min = v
	return(min,max)
print('list最小和最大值',findMinAndMan([1,2,3,-99,123,3123123])) 


# 列表生成式
Flist = [x * x for x in range(1,11)]
print('列表生成式',Flist)

# 两层for循环
FDlist = [m + n for m in 'fuck' for n in 'wjh']
print('使用两层循环，可以生成全排列', FDlist)

FOSlist = [d for d in os.listdir('.')]
print('列出当前目录下的所有文件和目录名', FOSlist)

# 列表生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
gList = (x * x for x in range(10))
print(gList)
print(next(gList))
for n in gList:
	print('列表生成器 gList', n)

# 斐波拉契数列
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		# generator 会不断中断
		yield b
		a, b = b,a+1
		n = n +1
	return 'done'

for d in fib(30):
	print('斐波拉契数列', d)

# map的用法
def mapFn(x):
	return x * x
mapList = map(mapFn, [1,2,3,4,5,7,8,9])
print('map', list(mapList))


# reduce的用法
def reduceFn(result,item):
	return result + item
print(reduce(reduceFn,[1,2,3,4,5,6]))

# filter的用法
def isOdd(n):
	return  n % 2 == 1
filterL = filter(isOdd,[1,2,3,4,5,6,7,8])
print(list(filterL))

# sorted排序
print('sorted abs',sorted([23,-56,234,-999,-123,33], key=abs))

# lazy fn
def lazy_sum(*args):
	def sum():
		ax = 0
		for x in args:
			ax += x
		return ax
	return sum
lazyFn = lazy_sum(10,25,30,55,65,2,1,3)
print('lazy function', lazyFn, lazyFn())

# 闭包 closure 
# 如count类型是int 需加nonlocal
def closureFn():
	count = [0]
	def countDone():
		count[0] += 1
		return count[0] 
	return countDone

closureFn1 = closureFn()
closureFn2 = closureFn()
print(closureFn1())
print(closureFn2())
print(closureFn2())

# 匿名函数
print(list(map(lambda x: x*x, [1,2,3,4,5,6,7])))

# 装饰器
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s()' % func.__name__)
		return func(*args, **kw) 
	return wrapper

@log
def new():
	print('2018-4-2')
new()

# 偏函数
int2 = functools.partial(int, base=2)
print('偏函数', int2('1000001'))

def testSys():
	args = sys.argv
	if len(args) == 1:
		print('sys args 1')
	elif len(args) == 2:
		print('sys args 2')
	else:
		print('too many args')
	print(args)
testSys()

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value, ',', member)

@unique
class Weekday(Enum):
	# 设定个day的value
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print('Weekday.Mon', day1, day1.value)
print('Weekday(1)', Weekday(1))
