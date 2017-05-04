## 前言
在 web 应用部署到线上后，需要保证应用一直处于运行状态，在遇到程序异常、报错等情况，导致 web 应用终止时，需要保证程序可以立刻重启，继续提供服务。

所以，就需要一个工具，时刻监控 web 应用的运行情况，管理该进程。

Supervisor 就是解决这种需求的工具，可以保证程序崩溃后，重新把程序启动起来等功能。


## Supervisor 简介
[Supervisor](https://github.com/Supervisor/supervisor) 是一个用 Python 写的进程管理工具，可以很方便的用来在 UNIX-like 系统（不支持 Windows）下启动、重启（自动重启程序）、关闭进程（不仅仅是 Python 进程）。

## 安装
1. Ubuntu系统下：`apt-get install supervisor`，通过这种方式安装后，自动设置为开机启动
2. 也可以通过 `pip install supervisor` 进行安装，但是需要手动启动，然后设置为开机启动（不推荐这种安装方式）

## Supervisor 配置
Supervisor 是一个 C/S 模型的程序，`supervisord` 是 server 端，`supervisorctl` 是 client 端。

### supervisord
下面介绍 supervisord 配置方法。supervisord 的配置文件默认位于 `/etc/supervisord.conf`，内容如下（`;`后面为注释）：
```
; supervisor config file

[unix_http_server]
file=/var/run/supervisor.sock   ; (the path to the socket file) UNIX socket 文件，supervisorctl 会使用
chmod=0700                       ; sockef file mode (default 0700) socket 文件的 mode，默认是 0700

[supervisord]
logfile=/var/log/supervisor/supervisord.log ; (main log file;default $CWD/supervisord.log) 日志文件，默认是 $CWD/supervisord.log
pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid) pid 文件
childlogdir=/var/log/supervisor            ; ('AUTO' child log dir, default $TEMP)

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock ; use a unix:// URL  for a unix socket 通过 UNIX socket 连接 supervisord，路径与 unix_http_server 部分的 file 一致

; 在增添需要管理的进程的配置文件时，推荐写到 `/etc/supervisor/conf.d/` 目录下，所以 `include` 项，就需要像如下配置。
; 包含其他的配置文件
[include]
files = /etc/supervisor/conf.d/*.conf ; 引入 `/etc/supervisor/conf.d/` 下的 `.conf` 文件
```

### program 配置
program 的配置文件就写在，supervisord 配置中 `include` 项的路径下：`/etc/supervisor/conf.d/`，然后 program 的配置文件命名规则推荐：app_name.conf

```
[program:app] ; 程序名称，在 supervisorctl 中通过这个值来对程序进行一系列的操作
autorestart=True      ; 程序异常退出后自动重启
autostart=True        ; 在 supervisord 启动的时候也自动启动
redirect_stderr=True  ; 把 stderr 重定向到 stdout，默认 false
environment=PATH="/home/app_env/bin"  ; 可以通过 environment 来添加需要的环境变量，一种常见的用法是使用指定的 virtualenv 环境
command=python server.py  ; 启动命令，与手动在命令行启动的命令是一样的
user=ubuntu           ; 用哪个用户启动
directory=/home/app/  ; 程序的启动目录
```
**需要注意：**  
- 用 supervisord 管理时，gunicorn 的 daemon 选项需要设置为 False
- 如果启动命令需要包含`workon`，修改environment参数：`environment=PATH="/home/username/.virtualenvs/myproject/bin"`

### supervisorctl 操作
supervisorctl 是 supervisord 的命令行客户端工具，使用的配置和 supervisord 一样，这里就不再说了。下面，主要介绍 supervisorctl 操作的常用命令：

输入命令 `supervisorctl` 进入 supervisorctl 的 shell 交互界面（还是纯命令行😓），就可以在下面输入命令了。：
- help                 # 查看帮助
- status               # 查看程序状态
- stop program_name    # 关闭 指定的程序
- start program_name   # 启动 指定的程序
- restart program_name # 重启 指定的程序
- tail -f program_name # 查看 该程序的日志
- update               # 重启配置文件修改过的程序（修改了配置，通过这个命令加载新的配置)

也可以直接通过 shell 命令操作：
- supervisorctl status
- supervisorctl update
- ...

## 参考
- [liyangliang 博客](http://liyangliang.me/posts/2015/06/using-supervisor/)
