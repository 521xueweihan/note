#coding:utf-8
#import functools.wraps
from functools import wraps
def log(func):
    '''
    纪录log
    '''
    #@wraps(func)
    def warp_func(x):
        return u'调用了{}方法，结果为：{}'.format(func.__name__, func(x))
    return warp_func

@log
def f(x):
    '''
    加1
    '''
    return x + 1

print f(1)
print '----'
print f.__doc__
