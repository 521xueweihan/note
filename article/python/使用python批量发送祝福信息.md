## 需求
明天就是中秋了，我想给微信上的好友，群发祝福信息。但是如果千篇一律简直太没有心意了，如果可以在祝福信息中加上接收信息者的昵称，那么就感觉比较有诚意了。

所以，我就想写个脚本替我完成这些事情！**声明：** 主要目的是研究微信相关的使用，如果想发**情谊满满**的祝福信息，那还是手打，最有诚意！

## 过程
### 1、登陆
第一个问题肯定是如果获得登陆的状态，从而可以操作登陆的微信号进行发送消息。

#### 网页版微信登陆原理
微信网页版是通过**手机扫码**，然后手机点击登陆后，网页版上的微信就登陆完成了！我觉得非常神奇，同时很费解是如果做到的。所以我查阅了[相关资料](http://www.jianshu.com/p/7f072ac61763)，结果如下：

> 访问[微信网页版](https://wx.qq.com/)，生成的二维码图片，其实是一个url，扫码之后会解析出来一个url。这个url形如：`https://login.weixin.qq.com/l/随机生成的全局唯一的字符串`

(可以使用支付宝扫这个二维码，然后选择在‘浏览器中打开’，就可以看到二维码代表的url了)

第一步：用户 A 访问微信网页版，微信服务器为这个会话生成一个全局唯一的 ID，上面的 URL 中`全局唯一的字符串`就是这个 ID，此时系统还不知道访问者是谁。

第二步：用户A打开自己的手机微信并扫描这个二维码，并提示用户是否确认登录。

第三步：手机上的微信是登录状态，用户点击确认登录后，手机上的微信客户端将微信账号和这个扫描得到的 ID 一起提交到服务器

第四步：服务器将这个 ID 和用户 A 的微信号绑定在一起，并通知网页版微信，这个 ID 对应的微信号为用户 A，网页版微信加载用户 A 的微信信息，至此，扫码登录全部流程完成，流程图如下：

![](http://o6r0c5t2r.bkt.clouddn.com/wechat-web-login.jpg)

#### 获取登陆二维码
弄清楚登陆步骤和原理，所以我第一步需要获取到**登陆的二维码图片**。

通过chrome分析页面中的元素，我最初以为可以像爬虫一样分析页面中的标签，把登陆二维码的图片的url获取过来就ok了。但是，一切并非这么简单：
- 登陆二维码是动态生成的获取回来：`<img class="img" mm-src="{{qrcodeUrl}}"  mm-src-load="qrcodeLoad" mm-src-parallel mm-src-timeout="10" mm-src-retry-count="2" src="https://res.wx.qq.com/zh_CN/htmledition/v2/images/img302bc5.gif">`，mm-src是个变量形如：`https://login.weixin.qq.com/qrcode/uuid`，而且uuid就是上面说的 ID （后面同一称作uuid）。

所以直接通过页面获取登陆二维码的想法就失败了，根据上面的分析，现在是需要获取uuid。

#### 获取uuid
在github找到了一篇这样的文章：[网页微信客户端封包大全](https://github.com/kitech/wxagent/blob/master/doc/protocol.md)，根据文中的描述可以写一个获取uuid的函数：

```python
# 请求的url
url = 'https://login.weixin.qq.com/jslogin'

# 请求参数
params = {
    'appid': 'wx782c26e4c19acffb',
    'fun': 'new',
    'lang': 'zh_CN',
    '_': int(time.time()),
}

# 使用request带着上面的参数和url就可以获得uuid了

# 成功时返回的文本：window.QRLogin.code = 200; window.QRLogin.uuid = "xxxxxxxx";
# 最后通过正则表达式解析，从而得到状态码和uuid
```

#### 根据uuid获取登陆二维码图片
后面我发现了一个好用网页版的微信库，可以用来完成登陆。而且有详细的文档，我这篇文章就不再继续写了，因为没什么意义。如果发现更好玩的再回来更新吧！

[微信网页登陆可以参考这个项目](https://github.com/Urinx/WeixinBot)（更好）

**终止**

## 参考
- [扫码登录是如何实现的？](http://www.jianshu.com/p/7f072ac61763)
- [网页微信客户端封包大全](https://github.com/kitech/wxagent/blob/master/doc/protocol.md)
- [0x5e写的查看被删的微信好友python脚本](https://github.com/0x5e/wechat-deleted-friends)
