# 背景
我正在做一个小项目，做好了打算上线，所有需要买个服务器，看了一圈，发现还是卖个vps合算。买了之后，进行了一些列的设置，这里记录一下，以便后面查看。

- 系统: ubuntu
- 内存：1G

## 一、更改时区
```
1. 运行tzselec
2. 选择亚洲 Asia，确认之后选择中国（China)，最后选择北京(Beijing)
3. 复制文件到/etc目录下：cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime
4. 更新时间：sudo ntpdate time.windows.com
```
**注意**：如果提示“sudo 无法解析主机名称”，解决办法：`/etc/hosts`中的`127.0.1.1`对应的值修改为`/etc/hostname`的值。

## 二、区域语言设置

1. 编辑文件:`sudo vi  /var/lib/locales/supported.d/local`

2. 写入相关内容,比如写入如下内容:
```
代码:
zh_CN.UTF-8 UTF-8
zh_CN GB2312
zh_CN.GBK GBK
en_US.UTF-8 UTF-8
fr_FR ISO-8859-1
zh_CN.GB18030 GB18030
```
这个文件是所有已经激活的区域语言的列表

3. 生成相关的locales:`sudo locale-gen --purge`

4. 编辑文件:`sudo vi /etc/default/locale`:

	```
	写入相关内容.比如,写入如下内容:

	代码:
	LANG="zh_CN.UTF-8"
	LANGUAGE="zh_CN:zh"
	LC_ALL="zh_CN.UTF-8"
	```

5. 完了重启电脑,终端中输入命令locale,看看命令是否报错,正常的结果如下:

## 三、添加用户
不要使用root用户操作，所以需要创建一个用户用于安装、管理系统。
### 1、添加用户

首先用adduser命令添加一个普通用户，命令如下：
```
#adduser tommy  //添加一个名为tommy的用户
#passwd tommy   //修改密码
Changing password for user tommy.
New UNIX password:     //在这里输入新密码
Retype new UNIX password:  //再次输入新密码
passwd: all authentication tokens updated successfully.
```

### 2、赋予root权限

**方法一**：修改 /etc/sudoers 文件，找到下面一行，把前面的注释（#）去掉
```
## Allows people in group wheel to run all commands

%wheel    ALL=(ALL)    ALL
```

然后修改用户，使其属于root组（wheel），命令如下：
`#usermod -g root tommy`

修改完毕，现在可以用tommy帐号登录，然后用命令 su - ，即可获得root权限进行操作。

**方法二**：修改 /etc/sudoers 文件，找到下面一行，在root下面添加一行，如下所示：
```
## Allow root to run any commands anywhere
root    ALL=(ALL)     ALL
tommy   ALL=(ALL)     ALL
```
修改完毕，现在可以用tommy帐号登录，然后用命令 `su -` ，即可获得root权限进行操作。

### 3、允许新建的用户远程登录(使用密码登陆)
用useradd新增的用户不能直接用ssh远程访问，需要修改ssh相关配置

```
vi /etc/ssh/sshd_config
内容添加，如下：
AllowUsers root@192.168.1.32 admin
多个用户用空格隔开
```

**注意**：su [user]切换到其他用户，但是不切换环境变量，su - [user]则是完整的切换到新的用户环境。(建议用`su -`)

### 4、使用key登陆
在.ssh目录下创建`authorized_keys`，并把登陆机器的pub_key内容填入。下次ssh登录时就不需要输入密码，并且安全性更高。

#### 参考
- [博客园的一篇博客](http://www.cnblogs.com/daizhuacai/archive/2013/01/17/2865132.html)

## 四、安装工具
- 安装编译所需要的基本库：`sudo apt-get install build-essential python-dev`

- 安装pip，git，mysql:
	- mysql: `sudo apt-get install mysql-server`
	- git: `sudo apt-get install git`
	- pip: `sudo apt-get install python-pip`

- 安装docker：`wget -qO- https://get.docker.com/ | sh` (都在root下执行)
	- [docker 安装ss](https://hub.docker.com/r/oddrationale/docker-shadowsocks/)
	- docker常用指令：重启——`service docker restart`；查看docker启动的容器——`ps -aux | grep docker`

#### 参考
- [docker入门](https://github.com/widuu/chinese_docker/blob/master/installation/ubuntu.md#Ubuntu%E5%AE%89%E8%A3%85Docker)
