## 简述
今天上线了一个简单的 [Page](http://hellogithub.com/)，没有什么功能就是一个展示页。

但是，我发现部署完，上线后，还要弄不少东西。下面就是我记录、整理的一些上线网站基本都会用到的网站和配置。

## 加入统计代码
这个是必做的，可以用来分析网站的流量和数据，下面两个网站二选一吧：
- [百度统计](https://tongji.baidu.com/web/welcome/login)
- [谷歌分析](https://analytics.google.com/analytics/web/)

步骤就是：在你的网站的每个网页加入一段统计代码。根据提示几下就能完成了。

之后你就可以在选择的统计网站中的控制面板中，看到你的网站访问、流量来源等数据。

## sitemap.xml
Sitemap 可方便网站管理员通知搜索引擎他们网站上有哪些可供抓取的网页。

在线免费生成网站：https://www.xml-sitemaps.com/

## robots.txt
robots.txt，用于表明您不希望搜索引擎抓取工具访问您网站上的哪些内容。

在线免费生成网站：http://tool.chinaz.com/robots/

## favicon.ico
所谓favicon，即Favorites Icon的缩写，顾名思义，便是其可以让浏览器的收藏夹中除显示相应的标题外，还以图标的方式区别不同的网站。

在线免费生成网站：http://www.bitbug.net/

## Nginx 相关配置
### 1. 配置上述的静态文件
例如，上述的三个文件都放在：`/path/static_file/` 目录下，那么 nginx 的示例配置如下：
```
location /favicon.ico {
	root   /path/static_file/;
	access_log  off;
}
location /robots.txt {
	root   /path/static_file/;
	access_log  off;
}
location /sitemap.xml {
	root   /path/static_file/;
	access_log  off;
}
```

### 2. “www”和“non-www”
例如：`www.hellogithub.com`（`www`） 和 `hellogithub.com`（`non-www`） 是两个不同的地址，但是我们希望于这两个地址访问的是同一内容（搜索引擎也推荐这么做），所以下面就是利用 nginx 配置，解决这一问题，`www` ——> `non-www`：
#### HTTP 解决办法
```
server {
    listen       80;
    server_name  www.example.com;
    return       301 http://example.com$request_uri;
}

server {
    listen       80;
    server_name  example.com;
    ...
}
```

#### HTTPS 解决办法
我的网站不支持 HTTPS 所以就没有实验这个方法。
```
server {
        listen 80;
        server_name www.domain.com;
        # $scheme will get the http protocol
        # and 301 is best practice for tablet, phone, desktop and seo
        return 301 $scheme://domain.com$request_uri;
}

server {
        listen 80;
        server_name domain.com;
        # here goes the rest of your config file
        # example
        location / {

            rewrite ^/cp/login?$ /cp/login.php last;
            # etc etc...

        }
}
```

## 参考
- [Nginx no-www to www and www to no-www](http://stackoverflow.com/questions/7947030/nginx-no-www-to-www-and-www-to-no-www)
