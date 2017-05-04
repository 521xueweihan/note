**注意：dct代表字典，key代表键值**

1.判断字典中某个键是否存在

_实现_

```python
dct.has_key(key)  #False
```

_更Pythonic方法_

```python
key in dct  #False
```

2.获取字典中的值 你想对key的value加1，首先你要判断key是否存在，不存在给一个默认值

_实现_

```python
if key not in dct:
    dct[key] = 0
dct[key] += 1
```

_更Pythonic方法_

```python
dct[key] = dct.get(key, 0) + 1
```

如果key存在则返回对应的value，如果不存在返回默认值（这里是0）

3.字典的value是可变对象 如果这个可变对象为list，你想初始化并修改它们。 _实现_

```python
for (key, value) in data:
    # 把key和value以元组的结构存到list中
    if key in dct:
        dct[key].append(value)
    else:
        dct[key] = [value]
```

_更Pythonic方法_

```python
for (key, value) in data:
    dct.setdefault(key, []).append(value)
```

_更更Pythonic方法_

```python
dct = defaultdict(list)  # 字典value的默认值为[]
for (key, value) in data：
    dct[key].append(value)
```

dct ＝ defaultdict(list) 等同于 dct.setdefault(key, []) 据说前者快。 [defaultdict详解](http://www.cnblogs.com/herbert/archive/2013/01/09/2852843.html)

4.合并两个字典

```python
a = {'a':1,'b':2}
b = {'c':3}

# 方法1
new_dict = a
new_dict.update(b)

# 方法2
new_dict = dict(a.items()+b.items())

# 方法3(Pythonic)
new_dict = dict(a, **b)
```

**如果合并两个字典的时候，如果两个字典有相同的key，则把value相加**

```python
from collections import Counter
a = {'a':1,'b':2}
b = {'a':1}

c = Counter(a) + Counter(b)  # 此时c为Counter对象
c = dict(c)  # 转变成字典
print c
# {'a': 2, 'b': 2}
```

参考:
- [python:字典剧本](http://blog.xiayf.cn/2013/01/04/Python-The-Dictionary-Playbook-cn/)
- [python中两个字典合并](http://www.cnblogs.com/dkblog/archive/2012/02/02/2336089.html)
- [合并字典时，相同key的value相加](https://segmentfault.com/q/1010000000683968)
