## 前言
我是个 Pythoner，开发工具一直使用的 JetBrains 的 PyCharm。我师傅告诉过我：一个程序员一定要有一个用的很 6 的 [IDE](http://baike.baidu.com/link?url=0vAWu0XuZR9RA-5PFE5EVAlMN6Sov56kIYPaPx2zXQabQhH3WwjKNhVVID455q-SlHoYMrtsZiZaETe66_sZfXJnmNdqAnS63Jhlvc-EsN_gfKn_TVZy7wMiyWrqtRc455zxPs3-Aj-8Whzw1eB6ZCaY98XI7UmFMfjaAgZCbeV9-y0BpvnAdvsZEbbVs3ks)，你的开发效率会提高很多，很多。。。

我从小白的时候就一直用 PyCharm，只有你没发现的功能，没有它没有集成的。但是功能越是强大的 IDE，上手到使用熟练的时间就越长。但是一切的付出都是值得的，因为后面它会极大的提高编码效率。所以我还是极力推荐。

- [免费社区版（不需要激活）](https://www.jetbrains.com/pycharm/download/download-thanks.html)
- [专业付费版（需要激活码）](https://www.jetbrains.com/pycharm/download/download-thanks.html)

因为本人一直使用的专业版，都是在网上找的激活码，但是最近好像反盗版的力度加强了，找不到可用的激活码了。去看了看购买的价格，我就重新开始了搜索盗版的道路。。。下面就是我找到的激活方法（使用盗版可耻，请面壁思过），**最后：如果不是屌丝的话，请购买正版。**

## 激活
**专业版是需要激活的，社区免费不需要。**

### 搭建激活服务器
下面的方法适用于激活所有JetBrains 旗下的产品，亲测 PyCharm2016。

登陆自己的服务器然后执行如下操作：
1. 下载一键部署脚本：`wget http://home.ustc.edu.cn/~mmmwhy/jetbrain.sh && sudo sh ./jetbrain.sh`，自动以 root 身份运行
2. 根据提示进行配置：
![](http://images2015.cnblogs.com/blog/759200/201704/759200-20170426173949881-819672940.png)


3. 打开 PyCharm 选择 License sever 激活方式，输入激活地址（上面脚本输出的：License sever）：
![](http://images2015.cnblogs.com/blog/759200/201704/759200-20170426174005272-1392444867.png)

4. 查看激活服务是否跑起来了：`sudo lsof -i  :104`，如果有输出就是成功了


### 其它方法
1. [lanyus blog](http://idea.lanyus.com/)
2. 可以留言或者私信我，我可以提供我搭建好的 license server 地址
