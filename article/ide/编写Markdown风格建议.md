# 编写Markdown建议
## 参考赋值
参考赋值`[]`用中文。例如：

**Old**
```
python进阶学习的资料：

[python进阶必读汇总][1]

[Dongweiming的Python高级编程][2]

[1]: http://www.dongwm.com/archives/pythonjin-jie-bi-du-hui-zong/  "python进阶必读汇总"

[2]: http://dongweiming.github.io/Expert-Python/#1  "Dongweiming的Python高级编程"
```

**New**
```
python进阶学习的资料：

[python进阶必读汇总][python进阶必读汇总]

[Dongweiming的Python高级编程][Dongweiming的Python高级编程]

[python进阶必读汇总]: http://www.dongwm.com/archives/pythonjin-jie-bi-du-hui-zong/  

[Dongweiming的Python高级编程]: http://dongweiming.github.io/Expert-Python/#1
```

## 链接
场景：我想用markdown记录一些网上的资源，方便我的查看和记录。  

**Old**
```
python进阶学习的资料：

[python进阶必读汇总](http://www.dongwm.com/archives/pythonjin-jie-bi-du-hui-zong/),

[Dongweiming的Python高级编程](http://dongweiming.github.io/Expert-Python/#1)
```

因为要记录的url太多而且长，这样导致在文章内容中太多url，导致不美观，不直观，且不利于维护。所以我就想：有没有可能以`变量`的方式管理url，参考了[markdown语法说明][1]

**New**

原来这种**变量赋值**的方式叫做：参考赋值，采用参考式之后:
```
python进阶学习的资料：

[python进阶必读汇总][1]

[Dongweiming的Python高级编程][2]

[1]: http://www.dongwm.com/archives/pythonjin-jie-bi-du-hui-zong/  "python进阶必读汇总"

[2]: http://dongweiming.github.io/Expert-Python/#1  "Dongweiming的Python高级编程"
```
url统一都放在最下面更好维护，更排除掉了无意义的url带来的干扰。

## 内跳转
场景：实现在一个页面中的跳转，用于目录页等需求。

实现：采用html加锚点的方法。
```
[1](#a)
2
3
4
5
6
<span id="a">a</span>
```
效果：
[图片](#picture)，会跳转到下面的标题为图片的部分

<span id="picture"></span>
## 图片
我推荐的风格也是采用'参考式'和链接的很像，语法又一些不同，我直接给出参考值的写法了：

```
显示图片：
![][pic1]

[pic1]: http://7xqirw.com1.z0.glb.clouddn.com/boomerang.png "回旋镖"
```

上面介绍了Markdown的插入图片语法，下面我简单的说一下，我用Markdown写文章的时候插入图片的流程：

首先申请一个[七牛][qiniu]的免费账号，当做图床。就是把图片上传到他家的云盘后，会外链地址。如下图

![pic1]

通过这个地址就可以访问你上传的那张图片了。

第一个好处是，图片不会说过几天显示不了了。因为，这个图片是在你的七牛云盘中，除非七牛出毛病否则哪个外链地址会一直有效！

第二个就是，如果你想要限制图片显示的宽和高，点击七牛中的数据处理---->图片处理---->新建图片样式，按照提示，就可以满足限制现实图片的宽和高了。效果如下图：

![pic2]

所以，我插入图片的流程是：把图片下在本地---->上传到七牛空间---->拿到外链地址---->以'参考式'插入文章中

## 参考：
- [Cmd Markdown 简明语法手册][reference1]
- [Markdown 语法说明][reference2]

[1]: http://wowubuntu.com/markdown/#link "markdown语法 链接篇"
[reference1]: https://www.zybuluo.com/mdeditor?url=https%3A%2F%2Fwww.zybuluo.com%2Fstatic%2Feditor%2Fmd-help.markdown "Cmd Markdown 简明语法手册"
[reference2]: http://wowubuntu.com/markdown/ "Markdown 语法说明"
[qiniu]: http://www.qiniu.com/ "七牛官网"
[pic1]: http://7xqirw.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-02-22%20%E4%B8%8B%E5%8D%885.29.50.png "图床演示"
[pic2]: http://7xqirw.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-02-22%20%E4%B8%8B%E5%8D%885.29.50.png-test "图片样式演示"
