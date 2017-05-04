1.修改MySQL的登录设置：

``` shell
vi /etc/my.cnf
```  

在[mysqld]的段中加上一句：skip-grant-tables 保存并且退出vi。  

2.重新启动mysqld

``` shell
# /etc/init.d/mysqld restart  ( service mysqld restart )
```

3.登录并修改MySQL的root密码  

``` sql
mysql> USE mysql ;
mysql> UPDATE user SET Password = password ( 'new-password' ) WHERE User = 'root' ;
mysql> flush privileges ;
mysql> quit
```


4.将MySQL的登录设置修改回来  

``` shell
# vi /etc/my.cnf
```

将刚才在
**[mysqld]**
的段中加上的
**skip-grant-tables**
删除
保存并且退出vi。

5.重新启动mysqld

``` shell
# /etc/init.d/mysqld restart   ( service mysqld restart )
```
