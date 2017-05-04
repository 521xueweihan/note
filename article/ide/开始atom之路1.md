### 祝大家新年快乐
我就是来卖个萌，逃～
![][5]

---
## 正文

我最开始用atom是因为它看起来比较酷，我工作中主力还是使用pycharm，毕竟atom只是一个编辑器。我一
般只是用atom来写Makedown的文件。随着我自己的博客上线，我以后用atom的频率会增加很多，所以我打
算，好好学习下atom的使用，方便我以后出去装逼～～其实我另外一个学习atom的目的是：我觉得每个程序
员都需要熟练的使用一个编辑器，因为很多时候我们都是在‘编辑’。

> 说在最前面：以下内容全部在mac下实践，其他操作系统可以试着把cmd(command)换成ctrl。

### 基本操作  
atom的基本操作，你只需要记住一个快捷键“cmd＋shift＋p”,然后在输入框中输入命令,回车。例如：打开设置
![快速输入命令][1]
**注意：以后说的输入命令，就是进入到这里输入命令**

### 必装的包  

好的编辑器，必须有丰富的扩充包，以便于满足不同的需求。atom的包还是很多的。

如何安装包：输入命令`install p`


#### python：  
*我个人推荐编辑和看python代码用pycharm，而且atom强大之处在于编辑前端的代码，以为可以直接调用
chrome的开发者模式：cmd＋alt＋i*  

autocomplete-python — *python代码补全*  
autocomplete-snippets － *自动补全自定义变量（v1.4自带)*

#### Markedown:  
*多说两句，我之所以学习和使用Markedown是因为:md(markedown)的文件可以随便转化成html或者pdf，
同时github上面ReadMe都是md文件，各种api接口说明——流行；用习惯了，还真的挺方便的。*  

markdown-scroll-sync － markedown预览时左右同步  
(atom v1.4自带了makedown语法高亮)

#### 美化界面：  
*atom的主题包含UI和`syntax`和`UI`两个Theme*

syntax Theme: solarized-dark-syntax  
seti-icons: 不同文件前面会有不同的小图标  
minimap: 侧边预览代码

---

### 常用快捷键
- **commmand＋shift＋p**  
打开命令窗口，可以运行各种菜单功能  
- **分屏**  
atom默认的自动分屏快捷键，有冲突。解决办法。输入命令:`keymap` 在这个文件中设置快捷键
格式如下：  

	```
	# 分屏的快捷键映射
	'.editor':
		'ctrl-f9':'pane:split-up'  # 我的ctrl＋f9是分屏到下方
		'ctrl-f10':'pane:split-down'
		'ctrl-f11':'pane:split-left'
		'ctrl-f12':'pane:split-right'

	```  
- **cmd＋w**  
关闭当前tab
- **ctrl＋shift＋m**  
makedown文件预览
- **command＋t**  
多文件切换
- **command＋\**  
关闭左边的file-tree-view
- **ctrl＋g**  
文件内跳转到指定行
- **command＋f**  
文件内查找和替换
- **command＋shift＋f**  
多文件查找和替换
- **command＋［**  
对选中内容向左缩进
- **command＋］**  
对选中内容向右缩进  
- **command＋，**  
打开设置
- **cmd＋.**  
开启／取消按键绑定

---

### 基本设置
看完上面的内容，你最好去写一篇博客，或者敲敲代码。之所以我把基本设置放在这里说，是因为当你在使用
过程中，会发现有些地方不符合你的习惯。这个时候你就知道你想要什么，然后我这在引个路你就可以定制出
适合自己的设置了。

1. 基本的用到设置都setting中，扫一遍看看有什么需要改的。  
2. 如果你想改的东西在setting中没有找到，那就输入命令：`packages`，包中的setting找一找。  
**例如：** 我不像看见忽略的文件，图中灰色的文件
![例子1][3]

	输入命令：`packages` 再搜索：`tree view`。如下图：  
![例子2][4]  
进到里面钩上：Hide Ignored Names和Hide VCS Ignored Files 就ok了。其实atom很多功能都是
包来提供的，所以通过包来自定义  
3. 通过修改config文件来设置(以后再说)  

### 最后
atom还是一个很酷的编辑器，我也是刚入门摸着石头过河，希望这篇入门级别的文章能够给你带来一定的帮助
那真是太好了！  
好了，开始你的atom之旅吧～
---

### 推荐阅读：  
- [atom中文文档](https://github.com/guo-yu/atom-guide)
- [atom使用教程](http://wiki.jikexueyuan.com/project/atom/split-screen-operation.html)  
- 推荐mac下录制gif的软件：GifGrabber


[test]:http://7xqirw.com1.z0.glb.clouddn.com/8255800.jpeg
[1]:http://7xqirw.com1.z0.glb.clouddn.com/markedown1.png  

[2]:http://7xqirw.com1.z0.glb.clouddn.com/markdown2.png  

[3]:http://7xqirw.com1.z0.glb.clouddn.com/markdown3.png  
[4]:http://7xqirw.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-01-28%20%E4%B8%8B%E5%8D%885.29.55.png  
[5]: http://7xqirw.com1.z0.glb.clouddn.com/1%E6%9C%88%2029%2C%202016%2011%3A05.gif
