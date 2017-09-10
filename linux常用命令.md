# 查看版本
lsb_release -a


# 文件字符串批量替换
grep oldString -rl /path | xargs sed -i "s/oldString/newString/g"

# 递归删除某一类型文件
find . -name "*.bak" -type f -delete

## 查看端口被占用的情况
`sudo lsof -i:端口号`

**例如：**  
`sudo lsof -i:443`：查看 443 端口上的程序

## 查看进程
`ps -aux|grep 过滤关键字`

**例如：**  
`ps -aux|grep python`：列出所有 python 进程


## 创建软连接
`ln -s /path/source_filename softlink_filename`


# scp
scp someuser@192.168.199.1:/home/someuser/file ./    # 远程机器拷贝到本机
scp ./file someuser@192.168.199.1:/home/someuser/    # 拷贝到远程机器

# tar
tar zxvf FileName.tar.gz    # 解压
tar zcvf FileName.tar.gz DirName    # 压缩
