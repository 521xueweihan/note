# Python pip install mysql-connector-python 2.0.1 失败
如图：

![错误展示][1]

尝试了：pip install mysql-connector-python==2.0.1错误依旧

解决方法：

```bash
wget https://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.3.zip

unzip mysql-connector-python-2.0.3.zip

cd mysql-connector-python-2.0.3

python setup.py install
```

参照:[stackoverflow](http://stackoverflow.com/questions/27394426/python-pip-install-mysql-connector-python-2-0-1-fails)

[1]: http://7xqirw.com1.z0.glb.clouddn.com/759200-20160119121143078-554548811.png
