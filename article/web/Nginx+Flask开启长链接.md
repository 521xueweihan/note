## 长连接的好处
当访问一个页面时，需要加载静态文件和获取动态渲染出来的页面。也就是说访问一个页面其实是请求了很多次服务器，长链接就是可以减少这些请求建立链接的次数，复用一个连接，从而提高响应时间。


## Nginx 开启长连接
Nginx 配置如下：
```
http {
		...
        keepalive_timeout 30s;
        keepalive_requests 500;
		...
	}
```
现在响应已经开启了长连接，也就说访问首页是，加载静态文件和动态渲染的页面都是通过一个连接完成（keep-alive）的。响应时间得到了一定程度的优化。但是，Nginx 和 web application 之间还是短链接，下面就讲述如何实现，完整的长连接（Nginx与Application之间）


## 中间件选择
首先 Flask 是符合 WSGI 协议的框架，要解决并发问题，可以采用 WSGI 的中间件：`gunicorn`。但是这个中间件不支持 `http1.1`，长连接就是在 `http1.1` 版本引入的。所以，要是打算使用长连接，我这里就不是推荐 `gunicorn` 中间件（应用服务器）


可以通过另外的中间件——`uWSGI` 来实现 nginx 和 web application 的长连接，首先 `uWSGI` 兼容 WSGI 协议的框架，同时支持 `http1.1`。根据官方文档描述，效率是 `gunicorn` 的十倍。

Nginx 中修改配置如下：
```
location / {
	...
	proxy_redirect     off;
	proxy_pass         http://127.0.0.1:8888;
	proxy_http_version 1.1;
	proxy_set_header Connection "";
}
```

声明使用的 `http1.1`（默认为1.0），清空客户端请求时的自带 header 的 `Connection` 字段。
