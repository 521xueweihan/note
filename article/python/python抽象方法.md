## 抽象方法
我的理解抽象方法就是：父类的一个方法，继承的所有子类都必须要实现这个方法，否则报错。

## 举例说明
```python
class Base(object):
	def _method(self):
		raise NotImplementedError(u"出错了，你没有实现这个抽象方法")

class A(Base):
	def _method(self):
		print u"重写了这个方法，就不会报错了！"
```

这个例子，实现了抽象方法的功能。还有一个更加pythonic的方法，就是用`abc.ABCMeta`

## ABCMeta
```python
import abc
class Base(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def _method(self):
		return
```
父类通过定义`__metaclass__ = abc.ABCMeta`，然后通过`@abc.abstractmethod`装饰器修饰的方法，就变成了抽象方法了。如果子类不实现就会报错。
