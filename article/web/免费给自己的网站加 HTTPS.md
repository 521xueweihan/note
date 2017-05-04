## 简介
本文是通过 Let's Encrypt 提供的免费证书服务，实现让自己的网站加上 HTTPS。我的网站 —— [hellogithub](https://hellogithub.com/)，就是通过这种方式实现的 HTTPS。


## Let's Encrypt
Let's Encrypt 是一个于2015年三季度推出的数字证书认证机构，将通过旨在消除当前手动创建和安装证书的复杂过程的自动化流程，为安全网站提供免费的SSL/TLS证书。

通过 Let's Encrypt 提供的脚本和服务，可以**免费、方便** 地给自己的网站加上 HTTPS，步骤简单、方便快捷。

下面就一一道来，示例的操作环境如下：

> 系统版本：ubuntu 14.04，nginx 版本：nginx/1.4.6 (Ubuntu)

## 准备工作
1. 查看 nginx 版本：`nginx -v`
2. 查看 nginx 是否包含 `ssl` 模块：`2>&1 nginx -V | tr ' '  '\n'|grep ssl`
3. 检查 nginx 的重要配置：
```
user root;  ## 运行身份为 root
...
	server {
		# 后面用于 cerbot 验证网站的所有权
		location /.well-known/ {
			root /path;
		}
	}
...
```


## 步骤
#### 安装 certbot
1. 通过 Let's Encrypt 网站提供的 cerbot [安装教程](https://certbot.eff.org/)，选择自己的配置方式和操作系统。
2. 安装 certbot。
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot
```
3. 运行 certbot：`certbot certonly`，进入交互界面进行申请证书和验证网站的所有权。
4. 提高安全系数：`sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048`

#### 配置 nginx
下面以域名 example.com 为例：
```
server {
	listen 80;
	server_name example.com www.example.com;
	return 301 https://$host$request_uri;
}


server {
	listen 443 ssl;

	server_name example.com www.example.com;

	ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
	ssl_prefer_server_ciphers on;
	ssl_dhparam /etc/ssl/certs/dhparam.pem;
	ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
	ssl_session_timeout 1d;
	ssl_session_cache shared:SSL:50m;
	ssl_stapling on;
	ssl_stapling_verify on;
	add_header Strict-Transport-Security max-age=15768000;
	...
}
```

## 自动续签证书
Let's Encrypt 的证书 90 天过期，所以需要定期检查证书是否过期，同时续期。
1. 查看 cerbot 脚本位置：`sudo which cerbot`
2. 编辑 crontab ：`sudo crontab -e`
```
30 2 * * 6 /cerbot 脚本位置/certbot renew --dry-run >> /var/log/le-renew.log
35 2 * * 6 /usr/sbin/service nginx reload
```
每周六 2:30 检查证书，然后 2:35 重新加载 nginx 配置


## 参考
- [How To Secure Nginx with Let's Encrypt on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-14-04)
- [cerbot](https://certbot.eff.org/#ubuntutrusty-nginx)
- [查看 nginx 安装了哪些模块](http://blog.csdn.net/orangleliu/article/details/44219387)
