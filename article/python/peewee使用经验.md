# peewee 使用经验
>本文使用案例是基于 python2.7 实现

以下内容均为个人使用 peewee 的经验和遇到的坑，不会涉及过多的基本操作。所以，没有使用过 peewee，可以先阅读[文档](http://docs.peewee-orm.com/en/latest/index.html)

正确性和覆盖面有待提高，如果遇到新的问题欢迎讨论。

## 一、介绍
[Peewee](http://docs.peewee-orm.com/en/latest/index.html) 是一个简单、轻巧的 Python [ORM](https://zh.wikipedia.org/wiki/对象关系映射)。
- 简单、轻巧、富有表现力（原词 expressive ）的ORM
- 支持python版本 2.6+ 和 3.2+
- 支持数据库包括：sqlite， mysql and postgresql
- 包含一堆实用的扩展在 playhouse 模块中

总而言之，peewee 可以完全可以应付个人或企业的中小型项目的 Model 层，上手容易，功能很强大。

## 二、基本使用方法
```python
from peewee import *

db = SqliteDatabase('people.db')
class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.

class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()    
```
基本的使用方法，推荐阅读文档－－[quickstart](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)

## 三、推荐使用姿势
下面介绍一些我在使用过程的经验和遇到的坑，希望可以帮助大家更好的使用 peewee。

### 3.1 连接数据库
连接数据库时，推荐使用 playhouse 中的 db_url 模块。db_url 的 `connect` 方法可以通过传入的 URL 字符串，生成数据库连接。

#### 3.1.1 connect(url, \*\*connect_params)
通过传入的 url 字符串，创建一个数据库实例

**url形如**：  
- ```mysql://user:passwd@ip:port/my_db``` 将创建一个 本地 MySQL 的 my_db 数据库的实例（will create a MySQLDatabase instance）
- ```mysql+pool://user:passwd@ip:port/my_db?charset=utf8&max_connections=20&stale_timeout=300``` 将创建一个本地 MySQL 的 my_db 的连接池，最大连接数为20（[In a multi-threaded application, up to max_connections will be opened. Each thread (or, if using gevent, greenlet) will have it’s own connection.](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#connection-pool)），超时时间为300秒（will create a PooledMySQLDatabase instance）  
**注意：charset 默认为`utf8`。如需要支持 emoji ，charset 设置为`utf8mb4`**，同时保证创建数据库时的字符集设置正确```CREATE DATABASE mydatabase CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;```。

**支持的 schemes**：  
- apsw: APSWDatabase
- mysql: MySQLDatabase
- mysql+pool: PooledMySQLDatabase
- postgres: PostgresqlDatabase
- postgres+pool: PooledPostgresqlDatabase
- postgresext: PostgresqlExtDatabase
- postgresext+pool: PooledPostgresqlExtDatabase
- sqlite: SqliteDatabase
- sqliteext: SqliteExtDatabase
- sqlite+pool: PooledSqliteDatabase
- sqliteext+pool: PooledSqliteExtDatabase

#### 3.1.2 推荐姿势
```python
from playhouse.db_url import connect

from dock.common import config

＃ url: mysql+pool://root:root@127.0.0.1:3306/appmanage?max_connections=300&stale_timeout=300
mysql_config_url = config_dict.get('config').get('mysql').get('url')
db = connect(url=mysql_config_url)
```

**查看更多详情请移步官方文档：**[db-url](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#db-url)

### 3.2 连接池的使用
peewee 的连接池，使用时需要显式的关闭连接。下面先说下为什么，最后会给出推荐的使用方法，避免**进坑**。

#### 3.2.1 为什么要显式的关闭连接
>Connections will not be closed exactly when they exceed their stale_timeout. Instead, stale connections are only closed when a new connection is requested.

这里引用[官方文档的提示](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#pool-apis)。大致说：“超时连接不会自动关闭，只会在有新的请求时是才会关闭”。这里的`request`是指‘web 框架处理的请求’，peewee 源码片段：
```python
def _connect(self, *args, **kwargs):
    while True:
        try:
            # Remove the oldest connection from the heap.
            ts, conn = heapq.heappop(self._connections)  # _connections是连接实例的list(pool)
            key = self.conn_key(conn)
        except IndexError:
            ts = conn = None
            logger.debug('No connection available in pool.')
            break
        else:
            if self._is_closed(key, conn):
                # This connecton was closed, but since it was not stale
                # it got added back to the queue of available conns. We
                # then closed it and marked it as explicitly closed, so
                # it's safe to throw it away now.
                # (Because Database.close() calls Database._close()).
                logger.debug('Connection %s was closed.', key)
                ts = conn = None
                self._closed.discard(key)
            elif self.stale_timeout and self._is_stale(ts):
                # If we are attempting to check out a stale connection,
                # then close it. We don't need to mark it in the "closed"
                # set, because it is not in the list of available conns
                # anymore.
                logger.debug('Connection %s was stale, closing.', key)
                self._close(conn, True)
                self._closed.discard(key)
                ts = conn = None
            else:
                break
    if conn is None:
        if self.max_connections and (
                len(self._in_use) >= self.max_connections):
            raise ValueError('Exceeded maximum connections.')
        conn = super(PooledDatabase, self)._connect(*args, **kwargs)
        ts = time.time()
        key = self.conn_key(conn)
        logger.debug('Created new connection %s.', key)

    self._in_use[key] = ts  # 使用中的数据库连接实例dict
    return conn
```

根据 pool 库中的 `_connect` 方法的代码可知：每次在建立数据库连接时，会检查连接实例是否超时。但是需要注意一点：**使用中的数据库连接实例（\_in_use dict中的数据库连接实例)，是不会在创建数据库连接时，检查是否超时的**。

因为这段代码中，每次创建连接实例，都是在 `_connections`(pool) 取实例，如果有的话就判断是否超时；如果没有的话就新建。

然而，使用中的数据库连接并不在 `_connections` 中，所以每次创建数据库连接实例时，并没有检测使用中的数据库连接实例是否超时。

只有调用连接池实例的 `_close` 方法。执行这个方法后，才会把**使用后的**连接实例放回到 `_connections` (pool)。

```python
def _close(self, conn, close_conn=False):
    key = self.conn_key(conn)
    if close_conn:
        self._closed.add(key)
        super(PooledDatabase, self)._close(conn)  # 关闭数据库连接的方法
    elif key in self._in_use:
        ts = self._in_use[key]
        del self._in_use[key]
        if self.stale_timeout and self._is_stale(ts):   # 到这里才会判断_in_use中的连接实例是否超时
            logger.debug('Closing stale connection %s.', key)
            super(PooledDatabase, self)._close(conn)   # 超时的话，关闭数据库连接
        else:
            logger.debug('Returning %s to pool.', key)
            heapq.heappush(self._connections, (ts, conn))  # 没有超时的话，放回到pool中
```

#### 3.2.2 如果不显式的关闭连接，会出现的问题
如果不调用`_close`方法的话，**使用后** 的数据库连接就一直不会关闭(两个含义：回到pool中和关闭数据库连接)，这样会造成两个问题：
1. 每次都是新建数据库连接，因为 pool 中没有数据库连接实例。会导致稍微有一点并发量就会返回```Exceeded maximum connections.```错误
2. MySQL也是有 timeout 的，如果一个连接长时间没有请求的话，MySQL Server 就会关闭这个连接，但是，peewee的已建立（后面会解释为什么特指已建立的）的连接实例，并不知道 MySQL Server 已经关闭了，再去通过这个连接请求数据的话，就会返回 ```Error 2006: “MySQL server has gone away” ```错误，根据[官方文档](http://docs.peewee-orm.com/en/latest/peewee/database.html#error-2006-mysql-server-has-gone-away)

#### 3.2.3 推荐姿势
所以，每次操作完数据库就关闭连接实例。

- 用法1：使用with

    ```python
    def send_rule():
        with db.execution_context():
        # A new connection will be opened or, if using a connection pool,
        # pulled from the pool of available connections. Additionally, a
        # transaction will be started.
            for user in get_all_user():
                user_id = user['id']
                rule = Rule(user_id)
                rule_dict = rule.slack_rule(index)
                .....do something.....
    ```
- 用法2：使用Flask hook

    ```python
    @app.before_request
    def _db_connect():
        database.connect()
    #
    # This hook ensures that the connection is closed when we've finished
    # processing the request.
    @app.teardown_request
    def _db_close(exc):
        if not database.is_closed():
            database.close()
    #
    #
    # 更优雅的用法：
    from playhouse.flask_utils import FlaskDB
    from dock_fastgear.model.base import db
    #
    app = Flask(__name__)
    FlaskDB(app, db)  # 这样就自动做了上面的事情（具体实现可查看http://docs.peewee-orm.com/en/latest/peewee/playhouse.html?highlight=Flask%20DB#flask-utils）
    ```

**查看更多详情请移步官方文档：**[pool-apis](http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#pool-apis)

### 3.3 处理查询结果
这里没有什么大坑，就是有两点需要注意：

首先，查询的结果都是**该 Model 的 object，注意不是 dict**。如果想让结果为 dict，需要 `playhouse` 模块的工具方法进行转化：`from playhouse.shortcuts import model_to_dict`

其次，**`get`方法只会返回一条记录**

#### 3.3.1 推荐姿势
```python
from playhouse.shortcuts import model_to_dict
from model import HelloGitHub

def read_from_db(input_vol):
    content_list = []
    category_object_list = HelloGitHub.select(HelloGitHub.category).where(HelloGitHub.vol == input_vol)\
        .group_by(HelloGitHub.category).order_by(HelloGitHub.category)

    for fi_category_object in category_object_list:
        hellogithub = HelloGitHub.select()\
            .where((HelloGitHub.vol == input_vol)
                   & (HelloGitHub.category == fi_category_object.category))\
            .order_by(HelloGitHub.create_time)
        for fi_hellogithub in hellogithub:
            content_list.append(model_to_dict(fi_hellogithub))
    return content_list
```

## 四、常见错误及解决办法
### 4.1 'buffer' object has no attribute 'translate'
- 错误信息： "'buffer' object has no attribute 'translate'"
- 场景：BlobField  字段存储zlib compress压缩的数据
- 解决办法：需要指定pymysql的版本小于0.6.7 否则会报错
- [参考](https://github.com/coleifer/peewee/issues/871)

### 4.2 Can't connect to MySQL server Lost connection to MySQL server during query
- 错误信息：Can't connect to MySQL server Lost connection to MySQL server during query
- 场景：向 RDS 中插入数据
- 解决办法：因为请求的连接数过多，达到了 RDS  设置的连接数，所以需要调高 RDS 连接数
- [参考](https://github.com/PyMySQL/PyMySQL/issues/269)
