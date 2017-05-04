# python获取当前时间的前一天，前一周，前一个月。
实用python的datetime.timedelta方法，避免了有的月份是30和31等不同的情况。

获取前一个月的时间，方法实现：首先`datetime.datetime.now`获取当前时间，然后通过`datetime.timedelta`获取上一个月最后一天的datetime对象`dayto`，最后用`dayto`的数据初始化这个月的第一个天和最后一天的datetime对象。

```python
import datetime

d = datetime.datetime.now()

def day_get(d):
    oneday = datetime.timedelta(days=1)
    day = d - oneday
    date_from = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
    date_to = datetime.datetime(day.year, day.month, day.day, 23, 59, 59)
    print '---'.join([str(date_from), str(date_to)])

def week_get(d):
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    print '---'.join([str(date_from), str(date_to)])

def month_get(d):
    """    
    返回上个月第一个天和最后一天的日期时间
    :return
    date_from: 2016-01-01 00:00:00
    date_to: 2016-01-31 23:59:59
    """
    dayscount = datetime.timedelta(days=d.day)
    dayto = d - dayscount
    date_from = datetime.datetime(dayto.year, dayto.month, 1, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    print '---'.join([str(date_from), str(date_to)])
    return date_from, date_to
```

# 参考：
- [原址](http://www.oschina.net/code/snippet_736230_26816)
