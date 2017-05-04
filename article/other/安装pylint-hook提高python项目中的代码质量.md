### 什么是'git-pylint-commit-hook'
我在工作中，团队为了保证代码和提高代码的质量，要求每个项目都要求安装`git-pylint-commit-hook`，它是个钩子，会在你提交代码到本地版本库的时候，自动运行，根据配置文件`pylintrc`中设置的代码风格，去检测改动过的代码，并会对其进行评分，如果未达到设置的分数线，则这次提交到本地版本库的操作（commit），强制取消。需要修改代码后，评分超过设定的分数，才可以提交到本地版本库。

我发现这个是个很好的东西，所以就在自己的项目中也尝试安装使用，用来提高自己项目的代码质量。

### 安装步骤如下：

1. `cd 你的项目文件`，到你的项目根目录下（下面所有操作都是在项目根目录下操作）

2. `pip install -U git-pylint-commit-hook`，安装`git-pylint-commit-hook`钩子

3. 输入`mkdir .hooks/pre-commit`，初始化钩子

4. 输入`chmod 755 .hooks/pre-commit`，修改pre-commit权限，赋予可执行权限，并加入如下内容：
	```
	#!/bin/sh
# use pylint to check code,
# Requirements:
#       pip install git-pylint-commit-hook
#
git-pylint-commit-hook --limit=9.0 --pylintrc=.pylintrc
	```

	**limit参数就是设定的最低评分。**

5. 输入`touch .pylintrc`，创建配置文件，并加入内容：[pylintrc配置](https://gist.github.com/521xueweihan/fb39af36ecfc9900a53b3707357fda80)

6. 输入`ln -sf $(pwd)/.hooks/pre-commit .git/hooks/`，关联到github的commit事件，也就是执行commit指令时，自动运行`pre-commit`脚本。

### 最终效果
之后每次执行commit指令时，会自动对你的代码评分，如下图：

![](http://7xqirw.com1.z0.glb.clouddn.com/test%20pylint.png)

这个钩子并不能完全保证代码的质量，但是可以在一定程度上统一代码风格，从而提高项目的整体质量。刚开始，用的时候会有些不适应，就像俗话说的：“良药苦口利于病”。
