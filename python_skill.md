# 语法糖
## 装饰器
在不改动原函数代码的前提下，通过装饰器实现给原函数扩展功能（进行‘装饰’）。

下面为装饰器的示例代码：
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/5/5 上午10:32
#   Desc    :   装饰器
from functools import wraps

def hello(fn):
    def wrap():
        print 'hello'
        fn()
    return wrap


@hello
def simple_example():
    print 'world'


simple_example()


def add1(fn):
    # 装饰器不带参数，被装饰的函数结果＋1
    @wraps(fn)
    def wrap(*args):
        return fn(*args) + 1
    return wrap


def addnum(add_num):
    # 装饰器带参数，被装饰的函数结果＋add_num
    def real_decorator(fn):
        @wraps(fn)
        def wrap(*base_num):
            return fn(*base_num) + add_num
        return wrap
    return real_decorator


@add1
def value1():
    return 1


@add1
def value2(base_num):
    return base_num


@addnum(4)
def value3():
    return 1


@addnum(10)
def value4(base_num):
    return base_num

print value1()
print value1.__name__

print value2(2)
print value2.__name__

print value3()
print value3.__name__

print value4(4)
print value4.__name__

```

参考：
- http://coolshell.cn/articles/11265.html

## with
## 迭代器
## super
## 魔法方法

# 性能
## 生成器
## GIL
## 多线程
## 多进程
## 事件循环（event loop）
## Gevent
### gentlet

# Web
### WSGI
###

# 进阶必会库

# 工具
