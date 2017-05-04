# 起因
因为想重拾起linux，同时需要用docker起几个镜像，用来学习网络知识。本来想直接去阿里云上买，后来一想自己机器上，起一个linux是个不错的选择，毕竟不花钱！

还可以用来做本地测试，学习使用linux、docker等。记录下过程，防止以后忘记！（所以不会涉及具体的安装步骤）

## 下载
到[网易开源镜像站](http://mirrors.163.com/)，挑选一个linux下载。我安装linux只要是为了学习运维方面的知识，同时用于进行网络知识方面的实践。如果你跟我一样，推荐Ubuntu server版本，纯字符界面，就跟一个服务器一样。

安装时，注意：语言选择英文，否则会因为没有安装中文字体，显示字符会出现问题。其它的没有什么特别的直接一步步的走下来就行了。

ubuntu server语言选成中文，换回英文方法：
```
修改Ubuntu的配置文件/etc/default/locale
将原来的配置内容修改为
LANG=”en_US.UTF-8″
LANGUAGE=”en_US:en”
```
## 上手
VirtualBox（后面称作VB)中linux就是一个服务器，我不想直接在上面进行操作，因为上面什么都没有！所以直接采用ssh的方式，也就是使用真实的计算机操作VB中的linux。

首先，设置VB的网络，设置为NAT（我认为就是本地端口转发，用于与VM的通信）。如下：
![](http://7xqirw.com1.z0.glb.clouddn.com/nat.gif)

然后，设置端口转发，在真实机下操作：
- 方法1:直接输入：`VBoxManage modifyvm myserver --natpf1 "ssh,tcp,,3022,,22"`，`myserver`字段就是VM（虚拟机）的名字。例如我的就是‘learn_networking’。

- 方法2:保证VM在运行状态下，操作步骤如下：
![](http://7xqirw.com1.z0.glb.clouddn.com/%E8%AE%BE%E7%BD%AEssh.gif)

最后，在本机中输入：`ssh -p 3022 user@127.0.0.1`，‘user’字段就是linux中的用户名。连接成功如下：
![](http://7xqirw.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-05-05%20%E4%B8%8B%E5%8D%886.45.23.png)

最好修改下源（就是apt安装文件的时候去哪里找，否则通过apt安装软件会慢），[请参考](http://mirrors.163.com/.help/ubuntu.html)

## 他能干嘛？
它可以做一个本地的测试环境。比如，VM安装的环境和线上服务器一样。在开发完一个功能之后，通过git，可以先把新的代码部署到刚设置好的本地的VM上，然后在本地测试，如果没有问题，就可以上线了。

比如：VM起了一个服务，监听的是8000端口，本机上查看效果。我们就可以像上面一样，修改NAT，如果本机想通过`127.0.0.1:3008`访问VM上的服务，那么我就把NAT改成如下图所示：
![](http://7xqirw.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-05-05%20%E4%B8%8B%E5%8D%887.15.22.png)

最后，在VM用python的`SimpleHTTPServer`和`BaseHTTPServer`内建模块，写个简单的server脚本——'test.py'，用来演示上面设置的NAT是否成功。代码如下：
```python
import SimpleHTTPServer
import BaseHTTPServer

def test():
    BaseHTTPServer.test(SimpleHTTPServer.SimpleHTTPRequestHandler,
	                    BaseHTTPServer.HTTPServer)

# 默认监听：8000端口
test()
```
同目录下，写一个‘index.html’文件，因为`SimpleHTTPRequestHandler`，默认返回同目录下的`index.html`文件。
```html
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<h1> 我是削微寒的VM:xueweihan</h1>
<p>用来构建本地的测试环境、学习网络编程的知识、练习linux</p>
</body>
</html>
```

在VM中，执行`python test.py`，运行效果如下：
![](http://7xqirw.com1.z0.glb.clouddn.com/vm%20show.gif)

## 参考
- [如何设置NAT](http://stackoverflow.com/questions/5906441/how-to-ssh-to-a-virtualbox-guest-externally-through-a-host)
