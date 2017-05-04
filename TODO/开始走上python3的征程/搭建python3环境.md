## 为什么学习python3
一直有学习python3的想法，但是因为python2更好找工作，使用的更普遍，所以我开始的时候一直是学习python2。但是我越发认为python3才是以后的趋势，因为豆瓣这种大公司已经转向python3.5了。而且python之父也早就宣称不再兼容python2。最后一个‘压死骆驼的稻草’就是我搜索python cook book；有一本英文原版，排版特别好，代码高亮，pdf原版的电子书。唯一不足就是它是第三版（里面的代码使用python3实现）。我粗略的翻阅了一下，发现还是可以看懂的。同时我在github上面找到了其他python爱好者翻译的中文版，已经全部翻译完成了。

看来万事具备，就差我投身python3的怀抱了。好了，其实中间的问题还是有很多，但是畏首畏尾，那就太浪费时间了。一个字：“干！”

## 部署python3环境
1. 大多数*inux自带的都是python2.x所以需要先安装python3，mac下的安装很简单：
```
brew install python3
```
关于brew可以参考：[Homebrew参考][brew]

2. 借助virtualenv实现python3环境
先通过`which python3`找的path:
```
➜ which python3
/usr/local/bin/python3
```
得到python3的路径，然后使用virtualenv创建python3环境
```
virtualenv -p /usr/local/bin/python3 python3
# virtualenv -p(指定python版本) path(which得到的路径) 虚拟环境名称
```

3. 激活python3环境
```
➜ source python3/bin/activate
(python3)➜ python
Python 3.5.1 (default, Mar  3 2016, 11:05:10)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
正如上面结果显示的，在刚才创建的虚拟环境中输入`python`启动的就是python3.5.1

4. 退出虚拟环境
输入：`deactivate`就直接退出了，如果想要删除这个虚拟环境。在退出情况下，直接删除刚才创建的python3文件夹就可以了。

[brew]: http://brew.sh/index_zh-cn.html "Homebrew参考""
