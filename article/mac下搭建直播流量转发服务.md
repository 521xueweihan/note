
## 1、安装Nginx
增加对 nginx 的扩展;也就是从github上下载,home-brew对ngixnx的扩展

`brew tap homebrew/nginx`，

## 2、安装Nginx服务器和rtmp模块

`brew install nginx-full --with-rtmp-module`

如遇到以下错误：
1. mkdir: /usr/local/var/log/nginx: Permission denied，解决办法
```
sudo chown -R $(whoami) /usr/local

sudo chown -R $(whoami) /Library/Caches/Homebrew
```

## 3、修改nginx.conf这个配置文件，配置rtmp
与 http 同级，加入

```
rtmp {
    server {
        listen 1935;
        chunk_size 131072;
        max_message 256M;
        application app {
            live on;
            record off;
            meta copy;
            push rtmp://直播地址;
        }
    }
}
```

## 问题
还没有成功，现在的问题：
- 感觉应该是xbox 上的网路设置，不应该设置dns，应该设置网关
- 数据包转发没有生效

## 待阅读
[Ran Aizen的《计算机网络》课程笔记](https://github.com/abbshr/Notes-HIT_computer_network/wiki)


## 参考
- [从xbox one直接推流到国内直播平台，无需采集卡](http://www.xbox-skyer.com/showthread.php?t=483001)
- [PF详细介绍](https://pleiades.ucsc.edu/hyades/PF_on_Mac_OS_X)
- [Mac 转发 PS4 twitch 直播流量到第三方直播平台](https://pohvii.blogspot.jp/2015/11/mac-ps4-twitch.html)
