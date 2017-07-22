# HelloGitHub.com 网站开源了

## 简介
随着 <a href="https://github.com/521xueweihan/HelloGitHub" target="\_blank">HelloGitHub</a> 月刊持续更新了一年多，内容变的越来越多。因为内容数据没有结构化，如果还是使用之前的编辑文本的方式编辑月刊内容，会对后面的继续发刊和维护带来了很多问题和多余的工作，例如：查看、查重、分类、排序、修改、同步内容等

**最初** 是使用本地数据库的方式进行管理数据，通过脚本生成内容，数据还是很容易出错。

**后面** 随着内容的增多，为了便于用户的分类查看，打算做个网站，利于展示和查阅。

**最后** 为了方便的管理展示的内容，同时**简化月刊的发布流程**，就打算开发个后台。

技术选型：
- Flask：轻量级 Python Web 开发框架
- Peewee：轻量级 Python ORM 库
- Purecss：轻量级 CSS 框架
- SQLite：轻量级数据库

网站效果：

![]()

<a href="https://hellogithub.com" target="\_blank">HelloGitHub.com</a>


## 为什么开源
首先本项目受益于开源，正是因为众多的开源库，使得我在开发这个网站的过程变的十分容易，难以想象没有这些开源的库。

其次，我的 HelloGitHub 月刊是推荐开源项目，那么这个网站开源也是必然的。

## 关于进阶
我发现在学习编程的过程中，入门资料十分的多，但是进阶的资料少之又少。这种现象不局限于某种语言，而是普遍想象。为什么会有这种显现呢？

入门是简单的，只要跟着输入指令得到预期的结果，就算过关。然而在入门阶段，很多概念不是那么容易理解，只是会使用或者说“照猫画虎”可以写出来。然后，当基础教程学习完成，打算动手写个项目的时候，发现寸步难行。然后就开始怀疑自己是否适合编程这条路，这就是为什么编程进阶的阶段会卡住很多人。

在讨论：“概念不理解”、“不知道写什么”这些问题之前，我觉得可以先讨论下：**编程是什么？**
>百度百科：让计算机为解决某个问题，对某个计算体系规定一定的运算方式，是计算体系按照该计算方式运行，并最终得到相应结果的过程。

简而言之，编程是为了让计算机帮助我们解决某个问题，而编程语言是与计算沟通的桥梁。这也就是说，所有的编程技巧和特性都是为了让我们更好的去解决**实际的问题**。

那么是否可以反思得出，入门时学习编程语言，一味的注重记住语法、而不去思考为什么会有这种特性和语法？就像学习汉子的过程，如果在学到一个新字时候，就去想在哪里见过、有什么词组、它是什么意思、如何使用它，而不是记住他详细的笔画。

拿编程中的面向对象举例：我在学习 Java 语言的时候，就接触到了面向对象，然后学习 Python 也遇到了这个概念。在介绍完这个概念就会学 “类” 这一章。每次到这一章，我就开始怀疑人生！我根本不懂面向对象的概念，就让我写类，我只能死记硬背、照猫画虎。随着照着写玩的代码可以跑了，随后而来的是我对编程失去信心了。

直到，我阅读、编写的代码量积累到一定的量的时候，我才真正的明白面向对象的意思：封装、继承，这给编程带来多大的便利。很多时候不是老师教授课的能力问题、自己的理解能力的问题。而是编程这门学科，在我看来是为了使用计算机解决实际问题而诞生的。所有的技巧都是为了更好的使用计算机解决问题，那么这些技术都是通过解决问题的过程中积累、总结而来的。如果不通过实际的理解使用，是无法理解这种技术的目的和优势的。

回到如何解决 “概念不理解”、“不知道写什么”这些问题，我的办法是**阅读、编写代码，用代码解决实际问题。** 在不会写代码的时候，多看别人怎么使用某一种编程问题去解决问题的；在写代码的过程中，要多看文档、错误信息；能写100行代码后，就考虑下这些代码有没有冗余的地方？如果让它变的更加易读和使用。

最后，这就是为什么我**推崇开源**的原因。正是丰富的开源资源让我学到了很多编程技巧同时融汇贯通、有意思的开源项目让我发现编程的乐趣，让我在编程的这条路上越走越远。

## 本项目的愿景
此项目基于 Flask 开发，现在只开发了一些基本功能，并没有集成 flask 的第三方库。现已发开的功能：
- OAuth 登陆
- 后台内容管理
- 前端异步展示

之所以如此简陋就选择开源。因为，我想呈现的就是从零到一的过程。在这个过程中，历经的开发、集成库、重构的过程和思想， 才是我想分享给大家的。通过上述的过程可以让新手更好的理解 开源思想、第三方库的优劣、Web 开发技术、开发流程 等。

我希望 hellogithub.com 这个项目可以做成一个系列教程，主要目的是：以实际 Web 开发项目为主要呈现，去理解、加入开源，发现编程的乐趣。

我认为**持续的自然成长才是进阶的解决之道**，而不可能是醍醐灌顶的飞跃。在学会了如何参与开源、使用开源社区的资源、解决问题的思路，在进阶的路上会越走越高，越走越顺畅。

## 如何启动本项目
1. 下载项目：`git clone https://github.com/521xueweihan/hellogithub.com.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 配置
4. 启动：`python server.py`

**配置步骤如下：**

在该目录下：`/项目地址/hellogithub.com/hellogithub/hellogithub/` 创建 `config.py`，配置内容如下：
```python
#/usr/bin/env python
# -*- coding:utf-8 -*-
from os import path

DEBUG = True
SECRET_KEY = 'test_secret_key'
STATIC_PATH = path.join(path.dirname(__file__), 'static')

PAGE_MAX = 5
GITHUB_IMAGE_URL = u'https://raw.githubusercontent.com/521xueweihan/HelloGitHub/{path}'
GITHUB_IMAGE_PREFIX = u'https://github.com/521xueweihan/HelloGitHub/blob/'
GITHUB_IMAGE_PATH_PREFIX = u'master/content/{volume_name}/img/{image_name}'

APP_DIR = '/项目地址/hellogithub.com/hellogithub'

GITHUB_TEMPLAT_PATH = path.join(APP_DIR, 'output_template/github_template.md')
GITBOOK_TEMPLAT_PATH = path.join(APP_DIR, 'output_template/gitbook_template.md')

DATABASE = 'sqliteext:///%s' % path.join(APP_DIR, 'test_hellogithub.db')


# GitHub OAuth local
CLIENT_ID = '02f1c617c1b20948b635'
CLIENT_SECRET = '2102c5c75d7482acf70a09317b697d6892380adc'
AUTHORIZE_URL = 'https://github.com/login/oauth/authorize/'
ACCESS_URL = 'https://github.com/login/oauth/access_token/'
```

**开启 admin 权限：**
- 登陆一次
- 修改数据库中 admin 字段为 1
- 注销，重新登陆
- 点击用户名即可跳转到管理后台

## 最后
我的前端技术很菜，需要前端小伙伴一起飞。同时，希望老司机也能带带我，对本项目和以后的规划提出建设性意见。
所以，我留下我的微信号，后面可能会拉个微信群一起交流，让这个项目能够帮助到更多的人。

- 我的微信号：xueweihan（请备注：hellogithub）
- 还有我是男的，我的头像是”朴信惠”
