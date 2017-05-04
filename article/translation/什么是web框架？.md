> 原文：[what is a web framework](http://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)

统一词汇：  
- web：网络
- application：应用（编程语言写的程序）
- web application：网络应用（编程语言写的程序，用于处理网络上的数据）
- request：请求
- response：响应

# 什么是web框架？
Web application frameworks(网络应用框架)，简称：web框架，用于构建web应用。不管是简单的博客网站，还是复杂的`AJAX`应用，每一个页面都是通过代码生成。我发现许多开发者喜欢学习web框架，像：`Flask`或`Django`。但是，他们却不真正理解什么是web框架、web框架的目的是什么、web框架是如何工作的。这篇文章，我将探究web框架中的那些不为人知的基本原理（通过探究，解答上面的三个问题）。读完这篇文章，你可以完全理解什么是web框架，为什么web框架这么重要。同时，你将能够：更快的理解一个新的框架；知晓一个框架的优劣，从而根据需求(实际情况)，选择更合适的框架。（这篇文章会让你真正的理解web框架，而不是只会用框架，按照文档‘按部就班’。）

## web框架如何工作的
在我们开始谈论web框架之前，我们需要知道**web是如何工作的**。我们将弄清楚：当你在浏览器中输入URL，按下回车，之后都发生了什么。在你的浏览器打开一个新的窗口，访问:`http://www.jeffknupp.com`(任何一个网址都可以，推荐：http://www.xueweihan.com 😊)。我们将一步步的来探究你的浏览器，在展示这个访问的页面过程中都做了什么。

### 1. web服务器
每个网页传都是以`HTML`格式传到你的浏览器，`HTML`是一种用于描述网页内容和结构的语言。响应并发送`HTML`给浏览器的**应用**叫做**web服务器**。容易令人迷惑的是：运行刚才所说的应用(响应并发送HTML给浏览器的应用)的**机器**也叫做**web服务器**。

需要注意，截止目前为止所有的服务器都是发送`HTML`给浏览器(**注意**：暂不考虑web服务器是发送Json给浏览器)。不论多么复杂的应用，最终结果都是发送`HTML`给浏览器。

web应用是怎么知道发送什么东西给浏览器？它是根据浏览器的请求返回响应的内容。

### 2. HTTP
浏览器通过HTTP协议向服务器请求网站的数据（HTTP协议在编程界是通用的、应用范围极广）。HTTP协议是‘请求－响应’模式的基础。客户端（浏览器）从服务器请求数据。web应用则是反过来响应客户的请求，发送响应数据给客户端（浏览器）。

需要记住的一点是：通信是有客户端（浏览器）发起的。服务器无法向客户端，启发（首先发起）连接或者主动发送数据给客户端。如果你接收到从服务器发来的数据，那么一定是你的浏览器请求的。

#### 2.1 HTTP方法
每一条信息都有一个方法和HTTP联系起来（换句话说：每个请求都需要一个指定HTTP方法）。不同的`HTTP`方法代表着不同的客户端请求逻辑和目的。以请求`HTML`网页为例(详情请参考：[form表单](http://www.w3school.com.cn/html/html_forms.asp))：
```html
<form action="接收这个请求的url" method="get或post">
	<li>姓名：<input type="text" name="name">
		<input type="subimt"/>
	</li>
</from>

```
提交表单有不同的逻辑，这两个不同的方法(method)用于两种不同的需求。

##### 2.1.1 HTTP GET方法
`GET`方法顾名思义：从服务器，得到(请求)数据。`GET`请求是最常见的`HTTP`请求。`GET`请求web应用的过程中只需要响应网页的HTML（内容），而不需要任何其他的额外操作。**注意**：`GET`请求不应该改变web应用的状态（例如：get不应该请求创建新的用户）。 原因是：`GET`请求通常被认为是“安全”的，因为它不修改网站的数据。

##### 2.1.2 HTTP POST方法
`POST`请求，它和网站有更多的交互，不像`GET`方法只是获取数据。我们也可以通过表单发送数据给web应用，只需要请求时：`method="post"`。`POST`请求是把用户的输入的数据，传递给web应用，例如：网站上的注册功能，就是在表单中把你的信息输入完成，然后通过`POST`方法，把这些数据发送给web应用，web应用在处理你的注册请求，返回注册成功或失败的结果。

`POST`请求会导致网站数据的改变。例如：通过`POST`表单，创建一个新的用户账号。`POST`请求的结果一般不请求接收新的HTML页面。而是，客户端根据响应的“响应状态码”做决定，例如：返回状态码200，代表服务器端操作成功，则客户端响应作出成功的操作。

#### 2.2 HTTP响应码
正常情况下，服务器返回响应码：200，代表着：“我做了你要求的任何事情，一切都很好。”响应码一般是三位数字。web应用必须给每个请求都返回请求的处理结果，响应状态码：200，意思是“OK”，通常用于响应`GET`请求。`POST`请求，可能接收到`204`（“没有内容”），意思是：“一起看起来没有问题，但是我还没有任何东西可以展示给你”。

**注意**：继续说上面`form`表单的例子，`POST`请求的地址，决定于`action`字段的值。也就是说：`POST`请求的地址，是由HTML页面中的字段决定的。

### 3. web应用
`GET`和`POST`方法是两个最常见的`HTTP`方法。web应用责任是：接收的`HTTP`请求，并返回相应的`HTTP`响应，返回的请求结果通常包含HTML。`POST`请求是让web应用做一些操作或者增加一条新的纪录到数据库。当然`HTTP`还有一些其他的方法，但是我们接下来只说`GET`和`POST`。

最简单的web应用是什么样？我们可以写一个监听`80`端口，等待连接（HTTP默认端口号就是80）的应用。它建立连接，等待接收客户端发来的请求，接收到请求后，返回一些简单的HTML作为响应。

最简单的web应用代码：

``` python
import socket

HOST = ''
PORT = 80
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
connection, address = listen_socket.accept()
request = connection.recv(1024)
connection.sendall("""HTTP/1.1 200 OK
Content-type: text/html


<html>
	<body>
		<h1>Hello, World!</h1>
	</body>
</html>""")
connection.close()
```
(如果上面的代码不能运行，尝试把端口号(PORT)更换为`8080`)

这段代码接收连接信号和请求信号，不管请求任何的URL，它都回复`HTTP 200`响应（所以这段代码不是一个真正的web服务器）。`Content-type: text/html`是头（header）字段，被用来表示请求和响应的元信息（meta-information:*元信息可用于浏览器（如何显示内容或重新加载页面），搜索引擎（关键词）[参考:meta](http://www.w3school.com.cn/html/html_head.asp)*)。这例子中，我们告诉客户端数据类型是HTML：`Content-type: text/html`（而不是JSON:`Content-Type: application/json`）。

#### 3.1 剖析Request
web应用接收到了请求，需要分析request，从而作出正确的处理。还需要返回正确的response，所以应用需要能够分析request和生成response，下面就说说什么是：request和response。

如果仔细观察`HTTP`请求，你会发现它和响应长的特别像。第一行是`<HTTP Method> <URL> <HTTP version>`(HTTP方法，请求的URL，HTTP协议版本)，例如：`GET / HTTP/1.1`。接下来，就是一些header（头）字段，例如：`Accept: */*`(意思是：可以接收任何类型的响应)。这里说的比较笼统，想要深究的同学可以参考：[HTTP真的很简单](http://www.cnblogs.com/xueweihan/p/5330189.html)

上面说了Request的格式，下面该说说Response的格式：`<HTTP version> <HTTP Status-Code> <Status-Code Reason-Phrase>`(HTTP协议版本，HTTP状态码，HTTP状态码描述)，例如：`HTTP/1.1 200 OK`。接下来和请求的格式一样，也是头字段，最后就是response包含的实际内容了。内容可以是字符串或者二进制对象（比如：图片和文件就是二进制对象），`Content-type`头字段指出了，内容类型，用于定义网络文件的类型，让客户端知道响应回来的数据类型，得到正确的响应结果。

#### 3.2 web服务器，还要做的杂活
如果我们要在上面那个**简单的web应用**的基础上继续，搭建出一个web应用，我们还需要解决以下几个问题：
1. 如何解析url使得，返回url对应的结果。（路由：route）
2. 如何在支持GET的基础上，支持POST。
3. 如何处理cookie和session。
4. 如何处理上千的并发量。

没有人愿意每次建立web应用的时候都需要去处理这些问题。所以，就出现解决这些问题和HTTP协议的packages（包）。记住：这些包的核心方法我们上面的例子是一样的：监听端口，接收请求，返回`HTTP`响应和HTML。

### 3.3 解决两个大问题：Routing(路由)和Templates(模版)
上面列出的建立web应用的问题，这里挑出两个：
1. 如何把请求的URL对应到处理这个请求的方法上？
2. 如何根据处理完的结果，动态的生成请求的HTML？

每一个web框架解决这两个问题用的都是不同的方式，有许多不同的方法。举例子说明，应该跟有助于理解。所以，下面我们讲讨论：Django和Flask的解决这两个问题的方法。在此之前，我们需要简单的说一下MVC模式。

#### 3.3.1 MVC在Django的应用
Django使用了MVC模式，MVC：“Model-View-Controller”(模型（Model）、视图（View）和控制器（Controller))，把应用中的逻辑分成三个部分。资源，数据库中的表相当于`Model`数据层。`Controller`控制器包含应用的业务逻辑和操作数据的操作。`View`视图，用于展示信息，动态的生成HTML，作为响应结果。

在Django中，控制器（Controller)被叫做视图（Views），视图（Views）被叫做模版（template）。这种叫法是有些奇怪，但是Django是一个简单，优雅的MVC结构的实现。

#### 3.3.2 Routing in Django(Django的路由)
路由是：把请求的URL和处理这个请求的代码，处理结果联系起来。拿咱们上面那个“最简单的web应用例子”来说，所有的请求，都是被同一段代码处理。正常的都是每个URL都有对应一个处理（handler）的函数，比如：我们访问`www.foo.com/bar`，它就对应`handle_bar()`函数，这个函数负责返回响应。我们可以把应用中的每个URLs都和一个方法一一对应起来。

如果请求的url中带有参数，我们如果获取url中的参数？并把参数传递给对应的处理函数？例如：`www.foo.com/users/3/`，我们想要显示user的id：3。

Django的解决办法是，通过正则表达式得到url中的的参数。比如：把url匹配`^/users/(?P<id>\d+)/$`的结果传入`display_user(id)`函数，这个`id`参数就是url匹配出来的结果。通过这种方法，形如：`/users/<some number>/`的URL都将调用`display_user`函数。

#### 3.3.3 Routing in Flask(Flask的路由)
Flask的路由管理机制和Django的有所不同，它使用的是`route()`装饰器。如下：
```python
@app.route('/users/<id:int>/')
def display_user(id):
	#...
```
这如上面所展示的，使用装饰器实现URL和方法的一一对应，更加简洁明了。参数通过`<name:type>`格式，专递给修饰的方法，静态的URLs比如：`/info/about_us.html`，你可以这样处理：`@app.route('/info/about_us.html')`。

#### 3.3.4 模版生成HTML
我们说完如何把‘URL和处理函数一一对应起来并传递参数到函数中’，这次我们需要把URL中的参数展示到页面上，也就是根据请求动态的生成页面（HTML）。Django和Flask都是用HTML模版来决解这种情况。

HTML模版类似于使用`str.format()`：它把动态的值（根据请求返回的值）有占位符来代替，最后输出的时候，再把通过`str.format()`函数，把占位符转化成具体的值。把一个页面想象成一个很长的字符串，里面的动态变量用占位符来替代，最后调用`str.format()`函数。Django和Flask使用的都是[jinjia2模版引擎](http://docs.jinkan.org/docs/jinja2/)。

模版引擎是为了动态生成页面，所以它的主要作用就是：生成一个模版，用于根据请求返回的值，生成页面，就像‘填空’。例如：模版内容：我是__程序员，而我想要展示：我是python程序员，而你没准想要显示：我是java程序员。具体实现，参考上面给的连接。

### 4. 数据交互
Django有着‘自带电池’的设计哲学，包含了ORM（对象关系映射：数据库中的表对应成代码中的类)，使得操作数据就像操作变得简单。Flask是‘微型框架’，它没有自带数据交互的模版，但是你可以使用[SQLAlchemy](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html)。Flask和Django通过使用ORM使得数据：增，删，改，查；变得十分方便，简单。

## web框架总结
到此为止，web框架到底做了什么就变得很清晰了：把`HTTP`的请求和响应，根据特定的规则对应到具体的处理函数上。把处理完的结果，传递到模版引擎上。Django和Flask是两个极端。Django包含了各种功能；Flask是‘微型框架’，只包含web框架的基本功能，但可以通过第三方包来扩充功能。

记住，Python web框架做的都是同样一件事情：接收`HTTP`请求，分配处理的方法，生成HTML作为`HTTP`响应，返回给客户端。实际上，几乎所有的web框架都是做了这些工作。但愿，你现在能够根据自己的需求，挑选最适合的框架了。
