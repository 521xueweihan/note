### mysql创建用户和授权  

#### 1.创建用户：  

(注意：下面的指令，请在root用户下输入)

``` sql
CREATE USER 用户名 IDENTIFIED BY '密码';
```  

如果要限制地址登录：  
例如只允许本地的用户登录@localhost  


``` sql
CREATE USER 用户名@地址 IDENTIFIED BY '密码';
```


**当mysql创建完用户之后，需要对该用户进行授权。授权之后，改用户才能有执行命令的权利！**
****

#### 2.授权

``` sql
GRANT ALL PRIVILEGES ON 数据库.* TO '用户名'@'登录主机' IDENTIFIED BY "密码";
```

* grant select,insert,update,delete on *.* to test1@"%" Identified by "abc";
* 格式：grant select on 数据库.* to 用户名@登录主机 identified by "密码"
* 如果想授权用户可以操作所有的数据：\*.\*(数据库写为：*)  

* 如果不限制登录主机：'用户名'@'%'(登录主机写为：%)

``` sql
FLUSH PRIVILEGES;
```
更新～
