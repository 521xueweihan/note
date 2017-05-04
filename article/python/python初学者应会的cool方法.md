##### [1, 2, 3, 4]变成数字：1234
使用高级函数reduce和lambda匿名函数：

```python
a = [1, 2, 3, 4]
a = reduce(lambda x,y: x*10+y, a)
type(a)  #int
a  #1234
```

##### 如何检验一个浮点数有没有小数部分
```python
a = 2.0
b = 2.1
a.is_integer()  #True
b.is_integer()  #False
```

##### 转置矩阵
```python
>>> mat = [[1,2,3],[4,5,6]]
>>> zip(*mat)
# 结果为：[(1,4),(2,5),(3,6)]
```

##### 两个单词时候是回文单词（排列不同的单词)
```python
from collections import Counter
def is_anagram(str1, str2):
	return Counter(str1) == Counter(str2)

>>> is_anagram('abcd', 'dbca')
True
>>> is_anagram('abcd', 'dbaa')
False
```

##### 不用任何循环，将嵌套列表转换成单一列表
```python
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> import itertools
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]
```

##### 手动输入字符串返回一个列表
输入：'1 2 3 4'，返回列表是[1, 2, 3, 4]  
注意：返回列表的元素是整数类型
```python
>>> result = map(lambda x:int(x), raw_input().split())
```
