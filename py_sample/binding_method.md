## python 绑定方法和非绑定方法

非绑定方法，用类名来引用方法例如：A.test()。如代码片段1:
```python
'''
代码片段1
'''
class A(object):
	def __init__(self):
		self.age = 1
	def age(self):
		print self.age
	def sex(self):
		print self.sex
		.
		.
		.

class B(A):
	A.__init__(self):
		A.test1()
		A.test2()
		.
		.
		.
```

这里就有一个问题了：当一个子类的父类发生变化时（如类B的父类由A变为C时），必须把子类中所有的通过
非绑定的方法的类名全部替换过来，例如代码段2，

```python
'''
代码片段2
'''
class C(object):
	def __init__(self):
		self.age = 1
		self.sex = 'man’
	def age(self):
		print self.age
	def sex(self):
		print self.sex
		.ssss
		.
		.

class B(C):
	A.__init__(self): # 都需要改成C.
		A.test1()
		A.test2()
		.
		.
		.
```
那么你就需要把B类中的所有（非绑定方法）A.都改成C.要是有一百个A.兄弟你就吐血去吧，这个时候就是
绑定方法上阵的时候了！就是这样，如代码片段3，

```python
'''
代码片段3
'''
class C(object):
	def __init__(self):
		self.age = 1
		self.sex = 'man’
	def test1(self):
		pass
	def test2(self):
		pass
	def test3(self):
		pass
		.
		.
		.

class B(C):
	super(C, self).__init__()
	self.test1()
	self.test2()
		.
		.
		.
```
