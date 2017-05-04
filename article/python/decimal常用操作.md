# decimal模块
## 简介
decimal意思为十进制，这个模块提供了十进制浮点运算支持。

## 常用方法
1.可以传递给Decimal整型或者字符串参数，**但不能是浮点数据，因为浮点数据本身就不准确。**

2.要从浮点数据转换为Decimal类型

```python
from decimal import *
Decimal.from_float(12.222)
# 结果为Decimal('12.2219999999999995310417943983338773250579833984375')
```

3.通过设定有效数字，限定结果样式：

```python
from decimal import *
getcontext().prec = 6
Decimal(1)/Decimal(7)
# 结果为Decimal('0.142857')，六个有效数字
```

4.四舍五入，保留几位小数

```python
from decimal import *
Decimal('50.5679').quantize(Decimal('0.00'))
# 结果为Decimal('50.57')，结果四舍五入保留了两位小数
```
