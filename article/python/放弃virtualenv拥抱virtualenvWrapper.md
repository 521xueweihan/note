## 什么是virtualenv
virtualenv是python的环境管理工具，用于隔离python的运行环境。也就是说，一个项目可以有一个属于这个项目的运行环境，从而避免了因为依赖不同的模块而产生的错误。

## 什么是virtualenvWrapper
virtualenv的升级版，更加有效的管理python的开发环境。可以查看所有的env和直接通过指令切换env，不需要输入路径之类的东西，更加统一、高效。

### 安装
1. `pip install virtualenvwrapper`
2. 把这行加入到shell环境中`source /usr/local/bin/virtualenvwrapper.sh`

### 常用指令
- 创建新的虚拟环境：`mkvirtualenv env名称`
- 切换环境：`workon env名称`
- 退出环境：`deactivate`
- 列出所有的环境：`lsvirtualenv`
- 删除环境：`rmvirtualenv`，注意：删除前退出删除的环境

更多指令：直接输入`virtualenvwrapper`，就会列出所有的指令和解释说明。
