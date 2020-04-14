# -*- coding: UTF-8 -*-
# 1.2 解压可迭代对象赋值给多个变量

a = (1,2,3,4,5)
x1, *x, x2 = a
print(f'{x1 = }')        # x1 = 1
print(f'{x  = }')        # x  = [2, 3, 4]
print('*x = ', *x)       # *x =  2 3 4
print(f'{x2 = }')        # x2 = 5

# 星号表达式在迭代元素为可变长元组的序列时是很有用的。
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 理解  x / *x / **x 的区别
def fun1(x, y = 'hello') : return (str(x) + str(y))
def fun2(**x) : return fun1(*x) # 此时的*x = (a, b) 是两个参数
def fun3(**x) : return fun1(x)  # 此时的x  = {'a': 1, 'b': 2} 是一个参数
def fun4(*x) :  return fun1(x)  # 此时的x  = (1, 2) 是一个参数
def fun5(*x) :  return fun1(*x) # 此时的*x = (1, 2) 是两个参数

print(fun2(a=1,b=2)) # ab
print(fun3(a=1,b=2)) # {'a': 1, 'b': 2}hello
print(fun4(1, 2))    # (1, 2)hello
print(fun5(1, 2))    # 12


