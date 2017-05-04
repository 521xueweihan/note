## 什么是 smb
服务器消息区块（英语：Server Message Block，缩写为SMB，服务器消息区块），又称网络文件共享系统（英语：Common Internet File System，缩写为CIFS），一种应用层网络传输协议，由微软开发，主要功能是使网络上的机器能够共享计算机文件、打印机、串行端口和通讯等资源。它也提供经认证的进程间通信机能。它主要用在装有Microsoft Windows的机器上，在这样的机器上被称为Microsoft Windows Network。  
经过Unix服务器厂商重新开发后，它可以用于连接Unix服务器和Windows客户机，执行打印和文件共享等任务。

## 挂载 smb
下面的命令均是在 ubuntu14.04 下执行通过。
1. `sudo apt-get install cifs-utils`
2. `sudo vi /etc/fstab`
3. 在 fstab 文件末位增加一行，用于设置开机自动挂载 smb：`//192.168.1.xxx/path /mnt/backups cifs uid=1000,gid=1000,username=xxx,password=xxx,sec=ntlm 0 2`
4. 重启机器：`sudo reboot`

注：通过 `id 用户名` 得到 uid 和 gid

## 卸载 smb
`sudo umount -l /mnt/backups`

## 适用场景
内网多处备份，相对于上传到s3等网盘服务，好处是节约带宽资源，同时有速度优势

## 参考
- [服务器消息区块](https://zh.wikipedia.org/wiki/%E4%BC%BA%E6%9C%8D%E5%99%A8%E8%A8%8A%E6%81%AF%E5%8D%80%E5%A1%8A)
- [centos6.2 挂windows共享目录报错问题解决 ](http://blog.sina.com.cn/s/blog_544f183101013zd7.html)
- [让linux挂载的移动硬盘具有执行权限](http://blog.sciencenet.cn/blog-430991-692444.html)
- [Linux操作系统里如何通过用户名查看UID、GID](http://liuleijsjx.iteye.com/blog/427245)
