# 撸一遍python的内建方法
这样做的好处就是：我如果要完成一个功能的时候，如果能用内建方法完成，就用内建方法。这样可以提高效率，同时使自己的代码更加优雅。哎呦？那岂不是撸完就是python高手了？我先帮大家试试效果，请静候我的反馈！

反馈：内建方法全部看完了，并敲完所有的内建方法，收获还是有的，但是发现不了解的知识更多了。内建方法属于python的标准库中的一章。python的标准库中还有很多值得一看的章节。[python2.7.8中文标准库文档](http://python.usyiyi.cn/python_278/library/index.html)，这些内容我粗略的看了一遍。这个内建方法的学习笔记我周三就写完了，本来想在写内建类型的学习笔记。但是发现太多了！而且我发现，看的太多记下的东西就会变少，所以我打算把重心转移到我自己练手的项目中（现在还没什么值得分享的东西，等拿得出手肯定会告诉大家的）。我想把学习标准库中收获的技巧用到我的项目中，这样学以致用才能真正融汇贯通。这就是我的下一步学习计划：通过实际项目，运用python标准库中的技巧！

结论就是：看完标准库我还没有成为高手，但是我收获了很多知识，基础牢固了一些。下一步打算在我自己的项目中运用这些技巧，提高自己的能力和技术！

相关资料
- [官方文档－内建方法(英文)－2.7.11][english]
- [官方文档－内建方法(中文)－2.7.8][chinese]

## 内建方法
| 常用内建方法     |        
| :------------- | :------------- | :------------- | :------------- |:------------- |
|[all](#all)|[divmod](＃divmod) |[input](#input)|[open](#open)|[staticmethod](#staticmethod)|
| [abs](#abs)  | [enumerate](#enumerate) |[int](#int)|[ord](#ord)|[str](#str) |
| [any](#any)  | [eval](#eval) |[isinstance](#isinstance)|[pow](#pow)|[sum](#sum) |
| [basestring](#basestring)  | [execfile](#execfile) |[issubclass](#issubclass)|[print](#print)|[super](#super) |
| [bin](#bin) | [file](#file) |[iter](#iter)|[property](#property)|[tuple](#tuple) |
| [bool](#bool) | [filter](#filter) |[len](#len)|[range](#range)|[type](#type) |
| [bytearray](#bytearray) | [float](#float) |[list](#list)|[raw_input](#raw_input)|[unichr](#unichr) |
| [callable](#callable)  | [format](#format) |[locals](#locals)|[reduce](#reduce)|[unicode](#unicode) |
| [chr](#chr)  | [frozenset](#frozenset) |[long](#long)|[reload](#reload)|[vars](#vars) |
| [classmethod](#classmethod)  | [getattr](#getattr) |[map](#map)|[repr](#repr)|[xrange](#xrange) |
| [cmp](#cmp)  | [globals](#globals) |[max](#max)|[reversed](#reversed)|[zip](#zip) |
| [compile](#compile)  | [hasattr](#hasattr) |[memoryview](#memoryview)|[round](#round)|[__import__](#__import__) |
| [complex](#complex)  | [hash](#hash) |[min](#min)|[set](#set)|[apply](#apply) |
| [delattr](#delattr)  | [help](#help) |[next](#next)|[setattr](#setattr)|[buffer](#buffer) |
| [dict](#dict)  | [hex](#hex) |[object](#object)|[slice](#slice)|[coerce](#coerce) |
| [dir](#dir)  | [id](#id) |[oct](#oct)|[sorted](#sorted)|[intern](#intern) |

__说明__:`[,xxx]`表示为可选参数。

<span id="abs"></span>
#### abs(x)
返回x的绝对值，例如：
```python
abs(-1.23) # 1.23
```

<span id="all"></span>
#### all(iterable)
如果iterable(迭代对象)的所有元素为真（或者iterable为空：[],'',()等），返回True。例如：
```python
all('') # True
all([1,2,3,0]) # False
```

<span id="any"></span>
#### any(iterable)
如果iterable中只要又一个元素为真，就返回True。例如：
```python
any([1,2,3,0]) # True
```

<span id="basestring"></span>
#### basestring()
它是str和unicode的超类，不能被调用或者实例化。只能用来测试一个对象是不是str或unicode的实例。例如：
```python
a = u'a'
b = 'b'
isinstance(a, basestring) # True
isinstance(b, basestring) # True
```

<span id="bin"></span>
#### bin()
将**整数**转成二进制**字符串**。
```python
bin(3) # '0b11'
```

<span id="bool"></span>
#### bool()
将一个值转化成布尔值。
```python
bool(1) # True
bool(0) # True
bool('') # False
bool(' ') # True
bool([]) # False
```

<span id="bytearray"></span>
#### bytearray()
结合memoryview，实现改变str类型对象的值。请移步[python内建类型](http://python.usyiyi.cn/python_278/library/stdtypes.html#memoryview-type)

<span id="callable"></span>
#### callable(object)
如果object参数可调用，返回True；否则返回False。对类的调用，返回一个新的实例。对于实例，如果实例有**call**方法，则该实例也是可以调用的。例如：
```python
class TestCallable(object):
	def __init__(self):
		pass

	def __call__(self):
		pass

callable(TestCallable) # True
callable(TestCallable()) # True
```

<span id="chr"></span>
#### chr(i)
返回一个字符，该字符的[ASCII][ASCII]码为整数i。i的取值范围：0 <= x < 255
```python
chr(100) # 'd'
ord('d') # 100
```

<span id="classmethod"></span>
#### classmethod(functions)
将传入的方法包装成类方法（类方法是指，类不需要实力化就可以直接调用的方法）。
类方法的第一个参数必须为类（约定俗称用cls代表），实例方法的第一个参数必须为实例（约定俗称为self），这两种接收参数的方法叫做：隐式第一参数（implicit first argument）。静态方法（通过@staticmethod装饰的方法)不需要如上述两个方法的隐式参数。
```python
class C(object):
	@classmethod
	def f(cls, arg1, arg2):
		pass
```
注意：通过@classmethod修饰的方法，为类方法。类可以直接调用（如C.f())；实例也可以直接调用（如C().f())，切记类方法中不能操作实例的属性。如果子类调用类方法，子类对象被传递为隐式的第一个参数（也就是cls为子类对象）。

<span id="cmp"></span>
#### cmp(x, y)
比较两个对象x和y，当`x < y`返回'-1'；`x > y`返回'1';`x == y`返回0
```python
cmo(1, 3) # -1
cmp(3, 1) # 1
cmp(1, 1) # 0
```
注意：`bool(-1)`结果为True

<span id="compile"></span>
#### compile(source, filename, mode)
compile可以将字符串或者Unicode字符串编译成代码对象。代码对象可以通过`exec`或`eval`执行。
- 参数source：字符串或者AST（Abstract Syntax Trees）对象。
- 参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
- 参数model：指定编译代码的种类。可以指定为 ‘exec’,’eval’,’single’。
```python
source ="if cmp(1, 1)==0: print 'yes'"
test_compile = compile(source, '', 'exec')
exec(test_compile)  #yes
```
注意：source是字符串，要注意引号和双引号，最后指定什么model，就用那种方法执行。compile返回的类型是`code`。

<span id="complex"></span>
#### complex(str)
创建一个复数。
```python
complex('1+2j') #可行
complex('1 + 2j') #报错(因为字符串中'+'或者'-'两遍不能有空白)
```

<span id="delattr"></span>
#### delattr(object, name)
参数是一个对象和一个字符串(`name`为字符串类型)，字符串必须是该对象的某个属性名。效果是：删除该对象的name对应的属性。
```python
class Test(object):
	def __init__(self):
		self.name = 'XueWeiHan'
test_delatter = Test()
test_delatter.name # XueWeiHan
delattr(test_delatter, 'name')
test_delatter.name # 报错，没有name属性，删除成功
```

<span id="dict"></span>
#### dict()
创建一个新字典。
```python
dict(a=1) # {'a': 1}
```
<span id="dir"></span>
### dir(object)
如果没有参数，返回当前本地作用域的名字列表。如果有参数，返回该参数的属性列表(属性和方法)。
如果类中定义了\__dir__方法，则`dir()`会先默认从\__dict__属性中收集信息。
```python
import time
type(time)  # model
dir(time)   # ['__doc__','__file__',...,'sleep','strftime',]就是time.可以调用的属性和方法
class TestDir(object):
	def __dir__(self):
		return ['TestDir1', 'TestDir2']
dir(TestDir)  # ['TestDir1', 'TestDir2']
```
注意：dir()主要是方便交互环境

<span id="divmod"></span>
### divmod(a, b)
效果：a除以b，返回商和余数的二元组（两个数组成的元组）
```python
divmod(5, 2)  #(2, 1)
```

<span id="enumerate"></span>
### enumerate(sequence, start=0)
返回一个枚举对象。sequence必须是序列，迭代器iterator，或者支持迭代的对象：
>迭代器Iterators:
迭代器仅是一容器对象，它实现了迭代器协议。它有两个基本方法：
1）next方法
返回容器的下一个元素
2）\__iter__方法
返回迭代器自身

```python
names = ['Xuweihan', 'James', 'Kobe']
enumerate_data = (names, start=0)  #这是个枚举类型数据
list(enumerate_data)  #[(0, 'Xuweihan'), (1, 'James'), (2, 'Kobe')]

list(enumerate(names, 1))  #[(1, 'Xuweihan'), (2, 'James'), (3, 'Kobe')]

# 实现
def enumerate(sequence, start=0):
	n =start
	for elem in sequence:
		yield n, elem
		n += 1
```
**注意**：enumerate是生成器，惰性计算。可以调用next()

<span id="eval"></span>
### eval(expression[,globals()[,locals()]])
expression参数被当作python表达式执行。使用`globals()`和`locals()`指定执行的代码中变量是全局变量还是本地变量。代码例子如下：
```python
a = 1  #全局变量

def add_one():
	a = 2  #本地变量
	eval('a+1', globals())  #结果为 2
	eval('a+1', locals())  #结果为 3
```

<span id="execfile"></span>
### execfile(filename[,globals[,locals]])
该函数类似exec（上面的那个），不同的是他解析一个**文件**，而不是字符串。它不同与\__import__语句的地方在于，它不使用模块管理——它无条件的读入文件且不会创建一个新模块。
(**不常用**)

<span id="file"></span>
### file()
file类型的构造函数。打开一个文件的时候，建议使用[open()](#open)而不使用`file()`。`file`更适合类型检测例如：`isinstance(f, file)`。

<span id="filter"></span>
### filter(functions, iterable)
构造一个列表，列表的元素来自于iterable，返回对于这些元素function返回`True`的元素。iterable可以是个序列，支持迭代的容器或者一个迭代器。
filter函数相当于过滤，返回符合functions的列表中的元素。带判断的列表生成式:`[i for i in list if i]`
```python
test_list = ['python', 'ruby', 'node.js']
result = filter((lambda x: x=='python'), test_list)  ＃结果：['python']
```

<span id="float"></span>
### float()
将字符串或者数字转化成浮点数。
```python
float('.3333')  #0.3333
float('a.333')  #报错
float(1)  #1.0
```

<span id="format"></span>
### format(value[,format_spec])
将value转化成“格式化”的表现形式，格式由`format_spec`控制。
```python
_string = '{name} is a pythoner'.format(name='Xueweihan')
print _string  # 'Xueweihan is a pythoner'
```

<span id="frozenset"></span>
### frozenset()
返回一个新的forzenset对象。就是一个不可变的集合，所以存在哈希值，可以作为字典的key。
**注意**：python的集合类型不支持整数。

<span id="getattr"></span>
### getattr(object, name[,default])
返回object的属性值。name必须是个字符串。如果名字指明的属性不存在，则返回default参数。

例如：`getattr(x, 'test')`等于x.test。

<span id="globals"></span>
### globals()
`globals(x)`，x成为全局变量。

<span id="hasattr"></span>
### hasattr(object, name)
参数是一个对象和一个字符串。如果对象含有该属性则返回True；否则返回False。


<span id="hash"></span>
### hash(object)
返回对象的hash值。hash值是整数，它被用于字典查找时快速比较字典的键。相同的数值有相同的hash（例如：1和1.0的hash值相同）

<span id="help"></span>
### help([object])
调用帮助系统（主要用于交互式的使用过程中）。如果没有指定object的话，则进入交互式的help帮助系统。

<span id="hex"></span>
### hex()
将number类型的数据，转化成“0x”打头小写的十六进制字符串：
```python
hex(33)  #'-0x21'

#float类型数据
float.hex(0.32)  #'0x1.47ae147ae147bp-2'
```

<span id="id"></span>
### id(object)
返回对象的“表示”，这是一个整数，在对象的生命期内**唯一且不变**。  
**注意**：CPython中：id就是对象的内存地址。
```python
id(33)  # 140300932661128

a = 33
id(a)  # 140300932661128

b = 33
id(b)  # 140300932661128
```

<span id="input"></span>
### input()
获取用户的输入。

建议用：raw_input

<span id="int"></span>
### int(x, base=10)
将数字或字符串x转化成一个整数，如果没有参数则返回0。

<span id="isinstance"></span>
### isinstance(object, classinfo)
如果参数object是参数classinfo的一个实例；或者是一个子类的实例，最终返回真。

推荐使用这个而不是用type进行判断。
```python
isinstance(1, int)  #True
```

<span id="issubclass"></span>
### issubclass(class, classinfo)
如果class是classinfo的子类，则返回真。

<span id="iter"></span>
### iter(o[,sentinel])
返回一个iterator(迭代器)对象。如果没有第二个参数，o必须是个集合独享，要么支持迭代协议[参考](#enumerate)，要么支持序列协议。例如：
```python
for x in [1, 2, 3]:
	pass

#等同于
it = iter([1, 2, 3])

while True:
	try:
		x = next(it)
	except StopIteration:
		break
```
如果有第二个参数sentinel，o必须是个可调用对象。使用场景：
```python
# 读取一个文件的行，直到读到特定行
with open('test.txt') as fp:
	for line in iter(fp.readline, ''):
		process_line(line)
```

<span id="len"></span>
### len(s)
返回对象的长度（元素的个数）。s可以是：序列或者集合。
```python
len('xueweihan')  #9
```

<span id="list"></span>
### list([iterable])
返回一个列表，其中的元素来自于iterable。iterable可以是个序列，支持迭代的容器，或者迭代器对象。
```python
list('xueweihan')  #['x', 'u', 'e', 'w', 'e', 'i', 'h', 'a', 'n']
```

<span id="locals"></span>
### locals()
把传入的变量，修饰成局部变量。

<span id="long"></span>
### long()
将一个字符串或者数字传化成一个长整数。

<span id="map"></span>
### map()
遍历iterable的每个元素，并把元素作为参数传入function，返回结果的列表。
```python
def add_two(num):
	return num+2
num_list = [1,2,3,4,5]
map(add_two, num_list) #[3,4,5,6,7]
```

<span id="max"></span>
### max()
返回可迭代的对象中最大的元素。

<span id="memoryview"></span>
### memoryview()
返回memoryview对象，它允许Python代码访问对象的内部数据而不用复制，只要该对象支持缓冲区协议。
如有疑问请参考[python内建类型memoryview](http://python.usyiyi.cn/python_278/library/stdtypes.html#memoryview-type)

<span id="min"></span>
### min()
返回可迭代的对象中的最小的元素。

<span id="next"></span>
### next(iterator[,default])
通过调用iterator(迭代器)的next()方法，得到它的下一个元素。如果有default参数，在迭代器迭代完之后返回该参数；否则抛出StopIteration。
```python
test_next_data = iter([1,2,3])
print next(test_next_data, 'Done')  #1
print next(test_next_data, 'Done')  #2
print next(test_next_data, 'Done')  #3
print next(test_next_data, 'Done')  #Done
```
**注意**:通过`iter()`返回的就是迭代器。

<span id="object"></span>
### object()
object是所有新式类的基类

```python
class A(object):
	pass
#继承于object的类为新式类
```

<span id="oct"></span>
### oct()
将任意一个整数转成一个八进制字符串。

<span id="open"></span>
### open(name, [,mode[,buffering]])
打开文件的方法，返回一个file类型对象。如果文件不能打开抛出IOError。  
mode：用什么方式打开文件。'r'读文件；'w'写文件；'a'附加。如果没有mode，默认是'r'。
buffering: 缓冲

<span id="ord"></span>
### ord()
参考：[chr()](#chr)

**注意**:如果是unicode,则返回unicode码

<span id="pow"></span>
### pow(x, y[,z])
返回x的y次幂：`x**y`  
如果有z参数：`(x**y) % z`

<span id="print"></span>
### print()
这个方法可以输出内容到file对象。  
**注意**:不常用，为了使print语句失效，而是用print()函数。（print和print()不是一个东西）可以在你的模块上面使用future语句：`from __future__ import print_function`

<span id="property"></span>
### property()
property其实就是个控制属性的权限的方法。同时实现，经property装饰的方法，可通过`Object.xxx`调用属性，把实例方法，变成实例的属性。这样做的好处是：可以在方法中实现限制条件，同时限制可执行的操作。
```python
class Student(object):
	def __init__(self):
		self._name = None
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
	if value != 'xueweihan':
		self._name = value
	@name.deleter
	def name(self):
		print 'del name!'
		del self._name
s = Student()
s.name = 'aaa'
s.name  #赋值成功'aaa'
s.name = 'xueweihan'
s.name  #赋值失败'aaa'
del s.name  #‘del name!’
```
**注意**:@property可以控制属性，比如只读属性：不实现@xxx.setter和@xxx.deleter就可以了。

<span id="range"></span>
### range(start, stop[,step])
用于创建列表，‘要头不要尾’。setp参数为步长
```python
range(5)  #[0, 1, 2, 3, 4]
range(2, 4)  #[2, 3]
range(10, 20, 5)  #[10, 15]
```

<span id="raw_input"></span>
### raw_input()
获取控制台的输入

<span id="reduce"></span>
### reduce(function,iterable[,initializer])
将带有两个参数的function累计地应用到iterable的元素上，从左向右。如果提供可选的参数initializer，它在计算时放在可迭代序列的最前面，并且当可迭代序列为空时作为默认值。例如：
```python
reduce((lambda x,y: x+y), [1, 2, 3, 4])
#相当于计算(((1+2)+3)+4)
```

<span id="reload"></span>
### reload(module)
如果你重新修改了模块，并且不打算停止重新启动python解释器的情况下使用该模块的最新版本。那么就使用`reload()`，在reload之前就**需要确保import过**。
```python
# test_reload.py
print 'a'

import test_reload  #'a'
#修改test_reload.py ——> print 'b'

import test_reload  #什么都输出，因为没有之前已经import过了，所以没有重新加载

reload(test_reload)  #'b'重新加载成功！
```

<span id="repr"></span>
### repr(object)
精准的返回某个对象可打印形式的字符串。返回的值，可以通过eval()执行。
```python
a = repr('a')  #"'a'"
```

<span id="reversed"></span>
### reversed(seq)
返回一个反向的**迭代器**。seq必须是一个具有\__reversed__()方法或支持序列协议的对象（实现\__len__()和\__getitem__()方法）。
```python
test_reverse = reversed([1, 2, 3, 4])  #<listreverseiterator object at 0x10bcab810>
test_reverse.next   #4
```
**注意**:可以编写一个定制的\__reversed__()方法的可能。

<span id="round"></span>
### round(number[, ndigits])
返回一个浮点数的近似值，保留小数点后`ndigits`位，默认`ndigits`为零。这个方法不好用，因为近似值不是**四舍五入**。
```python
round(2.675,2)  #2.67
```

<span id="set"></span>
### set([iterable])
返回一个集合对象，iterable是可迭代的对象。

<span id="setattr"></span>
### setattr(object,name,value)
给object的属性赋值，可以是存在的属性，也可以是不存的属性。例如：`setattr(s, 'name','xueweihan')`等同于`s.name='xueweihan'`

<span id="slice"></span>
### slice()
常用的切片方法：
```python
a = [1, 2, 3]
a[1:2]  #2
```

<span id="sorted"></span>
### sorted(iterable[,cmp[,key[,reverse]]])
用于iterable对象排序的方法。
- cmp指定一个自定义的带有两个参数的比较函数（可迭代的元素），它应该根据第一个参数是小于、等于还是大于第二个参数返回负数、零或者正数：cmp=lambda x,y: cmp(x.lower(), y.lower())。默认值是None。
- key指定一个带有一个参数的函数，它用于从每个列表元素选择一个比较的关键字：key=str.lower。默认值是None（直接比较元素）。
- reverse是一个布尔值。如果设置为True，那么列表元素以反向比较排序。


```python
class Student:
    def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
    def __repr__(self):
            return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)   # sort by age
#结果为：[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

<span id="staticmethod"></span>
### staticmethod(function)
返回一个静态方法。
```python
class C(object):
	@staticmethod
	def f(arg1, arg2):
		pass
```
**注意**:静态方法基可以在类上调用`C.f()`，也可以在实例上调用`C().f()`。

<span id="str"></span>
### str(object='')
返回一个字符串，包含对象的友好可打印表达形式。  
**注意**:`print`调用的就是对象的\__str__方法

<span id="sum"></span>
### sum(iterable[,start])
将iterable的元素从左向右相加并返回总和。
```python
sum([1, 2, 3])  #6
sum([1, 2, 3], 2)  #8
```

<span id="super"></span>
### super()
用于显性的指定父类的方法。同时实现方法的绑定。
```python
class C(B):
	def method(self, arg):
		super(C, self).method(arg)  #C的父类实例的method()
```

<span id="tuple"></span>
### tuple([iterable])
返回一个元素，元素顺序和iterable的元素相同。

<span id="tpye"></span>
### type(object)
返回object的类型。

type(name, bases, dict)
```python
class X(object):
	a = 1

X = type('X', (object,), dict(a=1))  # 当传入三个参数时，返回一个新的类型对象。
```

<span id="unichr"></span>
### unichr(i)
返回Unicode类型数据i的Unicode码。例如：`unichr(97)`返回字符串`u'a'`。

<span id="unicode"></span>
### unicode(object='')
返回object的Unicode版字符串

<span id="vars"></span>
### vars([object])
返回模块，类，实例或者其他任何具有\__dict__属性的对象的\__dict__属性。(key:value形式的\__dict__属性)

<span id="xrange"></span>
### xrange(x)
和[range()](#range)方法一样，区别就是它返回的是一个xrange对象而不是一个列表。惰性计算！当x很大的时候，一定要用xrange。

<span id="zip"></span>
### zip([iterable,...])
该函数返回一个元组的列表，其中第i个元素包含每个元素的序列的第i个元素。
```python
x = [1, 2, 3]
y = [4, 5, 6]
#可用于转置矩阵
zipped = zip(x, y)  #[(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zipped)
x == list(x2) and y == list(y2)  #True
```

<span id="_import_"></span>
### \__import__()
这种高级引入模块的方法，不常用，所以pass

[english]: https://docs.python.org/2/library/functions.html#all "官方文档－英文"
[chinese]: http://python.usyiyi.cn/python_278/library/functions.html "官方文档－中文"
[ASCII]: http://www.asciitable.com/ "ASCII表"
