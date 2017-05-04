## 概述
GPG是一种加密算法，现在github支持commit使用GPG加密，从而保证提交的commit在传输的过程中没有被篡改。

### 一、生成GPG密钥
什么是GPG：[阮一峰的GPG教程](http://www.ruanyifeng.com/blog/2013/07/gpg.html)
1. 安装GPG：`brew install GPG`

2. 生成GPG key：`gpg --gen-key`，根据提示，生成GPG key，注意：确保邮箱的那项是你github账号认证的邮箱；还有记住输入的密码。

3. 查看GPG key：`gpg --list-keys`，如下图：
![GPG list]
	注意：sub:私钥；pub:公钥；黄色的才是GPG key ID

4. 获取公钥：`gpg --armor --export pub GPG key ID`

### 二、github设置GPG key
1. 拷贝上面得到的公钥到github账号中，注意：格式如：开头：`-----BEGIN PGP PUBLIC KEY BLOCK-----`，结尾：`-----END PGP PUBLIC KEY BLOCK-----`。请参考[把GPG key 加到你的github帐号](https://help.github.com/articles/adding-a-new-gpg-key-to-your-github-account/)

### 三、配置git
1. 通过：`gpg --list-keys`查看pub GPG key ID，然后设置git签名时用的key：`git config --global user.signingkey pub GPG key ID`

2. 开启GPG签名commit：`git config commit.gpgsign true`；关闭：`git config commit.gpgsign false`

3. 如果你想让所有的本地仓库都使用GPG签名：`git config --global commit.gpgsign true`

### 四、效果
和正常的提交commit的区别，在开启commit使用GPG加密后，提交commit时，如下图：
![Signing commit]

push到github效果如下：
![Signing show]

## 参考
- [Signing commits using GPG
](https://help.github.com/articles/signing-commits-using-gpg/)
- [Generating a new GPG key](https://help.github.com/articles/generating-a-new-gpg-key/)
- [Telling Git about your GPG key](https://help.github.com/articles/telling-git-about-your-gpg-key/)



[GPG list]: http://7xqirw.com1.z0.glb.clouddn.com/gpg%20list.png "show GPG list"
[Signing commit]: http://7xqirw.com1.z0.glb.clouddn.com/gpg%20signing%20commit.png "GPG signing commit"
[Signing show]: http://7xqirw.com1.z0.glb.clouddn.com/GPG%20signing%20show.png "signing show"
