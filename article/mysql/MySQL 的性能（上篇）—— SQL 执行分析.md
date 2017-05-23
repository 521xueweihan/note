## 简介
> 文中内容均为阅读前辈的文章所整理而来，参考文章已在最后全指明

本文分为上下两篇：
- 上篇：MySQL 的 SQL 执行分析
- 下篇：MySQL 性能优化

后端开发必然会接触到数据库，数据层的优劣会影响整个服务的响应时间。所以，数据库的优化技巧是必须掌握的，下面就是我在学习过程中整理的，备忘。

## 一、SQL 执行时间分析
通过找到执行时间长的 SQL 语句，可以直观的发现数据层的效率问题。

### 1.通过 show processlist 来查看系统的执行情况
```
mysql> show processlist;
+----+------+-----------+------+---------+------+-------+------------------+
| Id | User | Host      | db   | Command | Time | State | Info             |
+----+------+-----------+------+---------+------+-------+------------------+
|  2 | root | localhost | NULL | Query   |    0 | init  | show processlist |
+----+------+-----------+------+---------+------+-------+------------------+
1 row in set (0.01 sec)
```

### 2.通过 profiling 来进行查看
这个命令是查看 SQL 的执行时间，能很直观的看出快慢。

#### 2.1 查看 profiling 是否开启
0 代表还是关闭着分析功能
```
mysql> select @@profiling;
+-------------+
| @@profiling |
+-------------+
|           0 |
+-------------+
```

#### 2.2 打开工具
```
mysql> set profiling=1;
Query OK, 0 rows affected, 1 warning (0.01 sec)

mysql> select @@profiling;
+-------------+
| @@profiling |
+-------------+
|           1 |
+-------------+
```

#### 2.3 查看 SQL 的执行时间
```
mysql> show profiles;
+----------+------------+----------------------------+
| Query_ID | Duration   | Query                      |
+----------+------------+----------------------------+
|        1 | 0.00173700 | select * from ip           |
|        2 | 0.00057500 | select porxy, port from ip |
+----------+------------+----------------------------+
```

#### 2.4 查看 SQL 执行耗时详细信息
语法：`show profile for query Query_ID`

```
mysql> show profile for query 1;
+----------------------+----------+
| Status               | Duration |
+----------------------+----------+
| starting             | 0.000073 |
| checking permissions | 0.000031 |   ---检查是否在缓存中  
| Opening tables       | 0.000207 |   ---打开表
| init                 | 0.000067 |   ---初始化
| System lock          | 0.000040 |   ---锁系统
| optimizing           | 0.000005 |   ---优化查询
| statistics           | 0.000021 |
| preparing            | 0.000015 |   ---准备
| executing            | 0.000003 |   ---执行
| Sending data         | 0.000993 |
| end                  | 0.000006 |
| query end            | 0.000007 |
| closing tables       | 0.000011 |
| freeing items        | 0.000169 |
| cleaning up          | 0.000089 |
+----------------------+----------+
```

以上具体的信息都是从 INFORMATION_SCHEMA.PROFILING 这张表中取得的。这张表记录了所有的各个步骤的执行时间及相关信息。语法：
`select * from INFORMATION_SCHEMA.PROFILING where query_id = Query_ID;`

### 3.慢查询日志
MySQL 的慢查询日志，顾名思义就是把执行时间超过设定值（默认为10s）的 SQL 记录到日志中。这项功能需要手动开启，但是开启后会造成一定的性能损耗。

### 3.1 查看慢日志是否开启
默认情况下slow_query_log的值为OFF，表示慢查询日志是禁用的，可以通过设置slow_query_log的值来开启。语法：`set global slow_query_log=1`

```
mysql> show variables  like '%slow_query_log%';
+---------------------+------------------------------------------------------+
| Variable_name       | Value                                                |
+---------------------+------------------------------------------------------+
| slow_query_log      | OFF                                                  |
| slow_query_log_file | /usr/local/var/mysql/xueweihandeMacBook-Air-slow.log |
+---------------------+------------------------------------------------------+
2 rows in set (0.11 sec)

mysql> set global slow_query_log=1;
Query OK, 0 rows affected (0.03 sec)

mysql> show variables  like '%slow_query_log%';
+---------------------+------------------------------------------------------+
| Variable_name       | Value                                                |
+---------------------+------------------------------------------------------+
| slow_query_log      | ON                                                   |
| slow_query_log_file | /usr/local/var/mysql/xueweihandeMacBook-Air-slow.log |
+---------------------+------------------------------------------------------+
```

### 3.2 设置超时时间
- 设置语法：`set global long_query_time=4`
- 查看语法：`show variables like 'long_query_time'`

**注意：修改后，需要重新连接或新开一个会话才能看到修改值。**

永久生效，修改 `my.cnf`
```
slow_query_log=1
long_query_time=10
slow_query_log_file=/path/mysql_slow.log
```

### 3.3 其他参数
#### 3.3.1 log_output
参数是指定日志的存储方式。log_output='FILE'表示将日志存入文件，默认值是'FILE'。log_output='TABLE'表示将日志存入数据库，这样日志信息就会被写入到mysql.slow_log表中。MySQL数据库支持同时两种日志存储方式，配置的时候以逗号隔开即可，如：log_output='FILE,TABLE'。日志记录到系统的专用日志表中，要比记录到文件耗费更多的系统资源，因此对于需要启用慢查询日志，又需要能够获得更高的系统性能，那么建议优先记录到文件。

#### 3.3.2 log-queries-not-using-indexes
未使用索引的查询也被记录到慢查询日志中（可选项）。如果调优的话，建议开启这个选项。另外，开启了这个参数，其实使用full index scan的sql也会被记录到慢查询日志。

#### 3.3.3 log_slow_admin_statements
表示是否将慢管理语句例如ANALYZE TABLE和ALTER TABLE等记入慢查询日志

### 3.4 分析工具 mysqldumpslow
MySQL 提供了慢日志分析工具 mysqldumpslow。

- `-s` 表示按照何种方式排序；
	- c: 访问计数
	- l: 锁定时间
	- r: 返回记录
	- t: 查询时间
	- al:平均锁定时间
	- ar:平均返回记录数
	- at:平均查询时间
- `-t` 是top n的意思，即为返回前面多少条的数据；
- `-g` 后边可以写一个正则匹配模式，大小写不敏感的；

#### 3.4.1 命令示例
- 得到返回记录集最多的 10 个 SQL：`mysqldumpslow -s r -t 10 /database/mysql/mysql06_slow.log`

- 得到访问次数最多的 10 个 SQL：`mysqldumpslow -s c -t 10 /database/mysql/mysql06_slow.log`

- 得到按照时间排序的前10条里面含有左连接的查询语句：`mysqldumpslow -s t -t 10 -g “left join” /database/mysql/mysql06_slow.log`

- 另外建议在使用这些命令时结合 | 和 more 使用 ，否则有可能出现刷屏的情况：`mysqldumpslow -s r -t 20 /mysqldata/mysql/mysql06-slow.log | more`

## 二、SQL 执行情况分析
使用 `explain` 分析 SQL 执行情况。

```
explain select * from ip;

+----+-------------+-------+------+---------------+------+---------+------+------+-------+
| id | select_type | table | type | possible_keys | key  | key_len | ref  | rows | Extra |
+----+-------------+-------+------+---------------+------+---------+------+------+-------+
|  1 | SIMPLE      | ip    | ALL  | NULL          | NULL | NULL    | NULL |  400 | NULL  |
+----+-------------+-------+------+---------------+------+---------+------+------+-------+
```

| select_type | table | type | possible_keys | key | key_len | rows | Extra |
| :---------- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 表示查询的类型| 输出结果集的表 | 表示表的连接类型 | 表示查询时，可能使用的索引 | 表示实际使用的索引 | 索引字段的长度 | 扫描出的行数(估算的行数) | 执行情况的描述和说明 |

## 参考
- [MYSQL中SQL执行分析](http://inter12.iteye.com/blog/1420789)
- [MySQL慢查询日志总结](http://www.cnblogs.com/kerrycode/p/5593204.html)
- [MySQL性能优化二](http://www.cnblogs.com/jiekzou/p/5380073.html)
