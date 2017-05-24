## 一、索引原理
### 1. 使用索引为什么会快?
btree类型的索引，就是使用的二分查找法，肯定快啊，算法复杂度是 `log2N`，也就是说16条数据查4次，32条数据查5次，64条数据查6次....依次类推。

btree 方式检索，算法复杂度： `log2N`

### 2. 索引的代价
1. 磁盘占用空间增多
2. 对dml(update delete insert)语句的效率影响

## 二、索引类型
简述mysql四种索引的区别：

1. `PRIMARY` 索引：在主键上自动创建
2. `UNIQUE` 索引： 只要是 UNIQUE 就是 Unique 索引。(只能在字段内容不重复的情况下，才能创建唯一索引)
3. `INDEX` 索引：普通索引
4. `FULLTEXT`：只在 MYISAM 存储引擎支持, 目的是全文索引，在内容系统中用的多，在全英文网站用多(英文词独立). 中文数据不常用，意义不大，国内全文索引通常使用 sphinx 来完成，全文索引只能在 `char`、`varchar`、`text` 字段创建

## 三、关于增加索引中的原则
- 根据where条件创建索引，select的字段不要包含什么索引（用＊号）
- 尽量的扩展索引，不要新建索引，不要过多用索引，索引列数最好在1-2。否则对表更新的效率有很大的影响，因为在操作表的时候要化大量时间花在创建索引中
- 对于复合索引，在查询使用时，最好将条件顺序按找索引的顺序，这样效率最高（最左匹配）
- 不要试图分别基于单个列建立多个单列索引（因为虽然有多个单列索引，但是MySQL只能用到其中的那个它认为似乎最有效率的单列索引）
- 索引列的类型越小查询效率越高
- 索引列不要进行运算

## 四、哪些列上适合添加索引
1. 较频繁的作为查询条件字段应该创建索引
2. 唯一性太差的字段不适合单独创建索引，即使频繁作为查询条件
3. 更新非常频繁的字段不适合创建索引
4. 不会出现在WHERE子句中的字段不该创建索引

## 五、索引常用操作
### 1. 添加PRIMARY KEY（主键索引）
```
mysql>ALTER TABLE `table_name` ADD PRIMARY KEY ( `column` )
```

### 2. 添加UNIQUE(唯一索引)
```
mysql>ALTER TABLE `table_name` ADD UNIQUE (`column`)
```

### 3. 添加INDEX(普通索引)
```
mysql>ALTER TABLE `table_name` ADD INDEX index_name ( `column` )
```

### 4. 添加FULLTEXT(全文索引)
```
mysql>ALTER TABLE `table_name` ADD FULLTEXT (`column`)
```

### 5. 添加多列索引
**注意**：当搜索时候需要多个条件作为条件是的时候使用多列索引，搜索条件可为：column1;column1,column2;column1,column2,column3;
```
mysql>ALTER TABLE `table_name` ADD INDEX index_name ( `column1`, `column2`, `column3` )
```

### 6. 查看索引  
```
mysql> show index from tblname;
```

### 7.删除索引
```
DROP INDEX index_name ON table_name
```

## 六、如何让索引生效
**查询要使用索引最重要的条件是查询条件中需要使用索引。**

可以通过 `explain`，查看 SQL 中的索引是否生效：
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

### 1. 下列几种情况下有可能使用到索引：
1. 对于创建的多列索引，只要查询条件使用了最左边的列，索引一般就会被使用。
2. 对于使用like的查询，查询如果是  '%aaa' 不会使用到索引， 'aaa%' 会使用到索引。

### 2. 下列的表将不使用索引：
1. 如果条件中有or，即使其中有条件带索引也不会使用。
2. 对于多列索引，不是使用的第一部分，则不会使用索引。
3. like 查询是以%开头
4. 如果列类型是字符串，那一定要在条件中将数据使用引号引用起来。否则不使用索引。(添加时,字符串必须'')
5. 如果mysql估计使用全表扫描要比使用索引快，则不使用索引。

## 参考
- [MySQL性能优化二](http://www.cnblogs.com/jiekzou/p/5380073.html)
- [MySQL单列索引和组合索引的选择效率与explain分析](http://blog.csdn.net/xtdhqdhq/article/details/17582779)
- [SQL Server的复合索引学习](http://www.cnblogs.com/bccu/archive/2007/08/14/855487.html)
