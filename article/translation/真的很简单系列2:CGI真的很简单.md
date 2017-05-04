> 原文：[CGI Made Really Easy](http://www.jmarshall.com/easy/cgi/)，在翻译的过程中，我增加了一些我在学习过程中找到的更合适的资料，和自己的一些理解。不能算是严格的翻译文章，应该算是我的看这篇文章的过程的随笔吧。

# CGI真的很简单
在此之前，你或许听说过很多说CGI‘晦涩难懂’的言论。如果你会写最基本的输入输出，那么你就可以写出一个CGI脚本。如果你已经是一个程序员，你只需要几分整就可以明白CGI到底是个什么东西。如果你还不是一个名程序员，对不起这篇文章不是很适合你，你可以先去学习一些编程的知识，例如脚本语言或者shell编程。但你学完了这些，再回过头来看！那么让我们开始吧！

这篇文章是写一个CGI脚本用于处理HTML提交的表单。虽然跳过了一些细节，但是可以让你在短时间内搞明白。

## 什么是CGI？
CGI不是一门编程语言。它是网页的表单和你写的程序之间通信的一种协议。可以用任何语言写一个CGI脚本，这些语言只要能接收输入输出信息，读取环境变量。所以，几乎所有的编程语言都能写一个CGI脚本，例如：python（把我大python放在第一个！），C，甚至是shell脚本。

## CGI脚本的结构
典型的CGI脚本做了如下的事情：
1. 读取用户提交表单的信息。
2. 处理这些信息（也就是实现业务）。
3. 输出，返回html响应（返回处理完的数据）。
下面主要解释，第一步和最后一步

## 读取用户提交的表单
当用户填写完表单，点击提交按钮的时候。CGI脚本接收用户表单的数据，这些数据都是k－v的集合的形式（也就是python中的字典）。这里有写实现的例子：[python](http://www.runoob.com/python/python-cgi.html)

如果你已经通过上面的例子看懂了，下面的就可以忽略了。如果你还有些不懂请看下面来那两个长的字符串。
- “name1=value1&name2=value2&name3=value3”
- "name1=value1;name2=value2;name3=value3"

区别就是：‘&’和‘;’这两个符号，他们的作用都是分隔参数。下面还有两件事情要做。

1. 把所有的‘＋’变成‘空格’
2. 把所有的符号都转译成‘％xx’样式的符号，例如：‘％3d’转化成‘＝’

这样做是为了统一用户的输入，使用统一的[URL-encoded][URL-encoded]进行转译。

那么你从哪里得到这些转译完的字符串呢？根据提交时的时候选用的是什么HTTP方法：
- GET方法，环境变量是通过URL来传递的，例如：我google‘URL encoded’ 点击搜索提交的请求就是： https://www.google.co.jp/search?q=URL+encoded（我省略其他一些干扰项，注意‘空格’转化成了‘＋’
- POST方法，通过HTTP消息主体传递的。**注意**:POST方法编码类型有：application/x-www-form-urlencoded 或 multipart/form-data。

我找了一个很好的资料，很短，一路了然：[POST对比GET方法][post-and-get]

总结：CGI接收的用户数据，是通过http协议传递过来的。而选用不同的‘Method’：GET或POST对CGI的接收没有任何影响。这段是让你明白：数据是怎么通过http协议传输的。

## 发送响应（Response)返回给用户
首先，第一行要写：`Content-type: text/html`

新起一行，用于输出数据。写好HTML响应页面。这个页面是：当你的脚本处理完数据后，返回给用户的结果。

是的，你可以随意编写返回的HTML代码。HTML很简单，而且方便。

## 我的总结
CGI是一种通信协议，它把用户传递过来的数据转变成一个k－v的字典。这个字典中不光有用户的数据，还有HTTP协议的参数。它做的就是把数据，组织成一个固定结构形式的数据。方便任何符合CGI协议的程序都可以调用！但是CGI不是负责通信（传输数据）的，通信的话是通过socket，也就是`server`，例如上面例子中，是通过Apache进行通信。之后调用CGI脚本，把数据转变成符合CGI协议的数据结构，用于后面的数据处理！

**这个系列文章完成后，后面还有一个实战系列。从头写一个web服务器，敬请期待！**


[URL-encoded]: http://www.ruanyifeng.com/blog/2010/02/url_encoding.html "url-encoded"
[post-and-get]: http://www.w3school.com.cn/tags/html_ref_httpmethods.asp "post and get"
