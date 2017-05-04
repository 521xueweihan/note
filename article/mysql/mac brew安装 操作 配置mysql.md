#### brew 安装 配置 操作 mysql
brew install mysql (安装)  
添加修改mysql配置  
mysqld --help --verbose | more (查看帮助, 按空格下翻)

你会看到开始的这一行(表示配置文件默认读取顺序)

Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /usr/local/etc/my.cnf ~/.my.cnf

通常这些位置是没有配置文件的, 所以要自己建一个

``` shell
ls $(brew --prefix mysql)/support-files/my-* (用这个可以找到样例.cnf)  
```

``` shell
cp /usr/local/opt/mysql/support-files/my-default.cnf /etc/my.cnf (拷贝到第一个默认读取目录)
```

按需修改my.cnf

brew services start mysql (启动)
brew services stop mysql (停止)

#### 中文问题：
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
