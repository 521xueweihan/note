1. linux文件名，不能带`:`，因为系统会认为带`:`的是远程的文件（时间会带`:`）
2. 备份时需要压缩文件使用`sudo tar -pczvf application-backup.tar.gz installdir`，其中`p`参数是带权限信息
3. 恢复时`sudo tar -pxzvf application-backup.tar.gz -C /path`，其中`C`参数后跟想要解压到路径
4. 通过`crontab` 命令定时启动备份脚本，注意指定对用户（例如上面的命令就需要在root用户下）
5. shell 执行过程的信息要记录下来，用于排错。可以通过重定向命令，输出到一个文件，`>>`为追加模式

## 示例
我写了一个 Gitlab 的备份脚本，应为安装的是 bitnami 的安装包，所以根据 bitnami 的文档中给出的备份方案，写脚本。下面先贴出文档中的原文。

---

## How To Create A Full Backup Of GitLab?
>https://docs.bitnami.com/installer/apps/gitlab/#how-to-create-a-full-backup-of-gitlab

### Backup
The Bitnami Gitlab Stack is self-contained and the simplest option for performing a backup is to copy or compress the Bitnami stack installation directory. To do so in a safe manner, you will need to stop all servers, so this method may not be appropriate if you have people accessing the application continuously.

Follow these steps:

- Change to the directory in which you wish to save your backup:

  ```
  cd /your/directory
  ```

- Stop all servers using the graphical manager or the command-line script. Here's an example:

  ```
  sudo installdir/ctlscript.sh stop
  ```

- Create a compressed file with the stack contents using a tool like 7-Zip or Winzip (on Windows) or a command like the one below (on Linux and Mac OS X):

  ```
  sudo tar -pczvf application-backup.tar.gz installdir (on Linux and Mac OS X)
  ```
- Restart all servers using the graphical manager or the command-line script:

  ```
  sudo installdir/ctlscript.sh start
  ```

You should now download or transfer the application-backup.tar.gz file to a safe location.

## Restore
Follow these steps:

- Change to the directory containing your backup:
  ```
  cd /your/directory
  ```

- Stop all servers using the graphical manager or the command-line script. Here's an example:
  ```
  sudo installdir/ctlscript.sh stop
  ```

- Move the current stack to a different location:
  ```
  sudo mv installdir /tmp/bitnami-backup (on Linux and Mac OS X)
  move installdir C:\Windows\Temp (on Windows)
  ```

- Uncompress the backup file to the original directory using a tool like 7-Zip or Winzip (on Windows) or a command like the one below (on Linux and Mac OS X):
  ```
  sudo tar -pxzvf application-backup.tar.gz -C /
  ```

- Start all servers using the graphical manager or the command-line script:
  ```
  sudo installdir/ctlscript.sh start
  ```

>IMPORTANT: When restoring, remember to maintain the original permissions for the files and folders. For example, if you originally installed the stack as the root user on Linux, make sure that the restored files are owned by root as well.

---


## 代码
根据文档中所述，把上面的命令写成 python 脚本，用于定期执行。代码如下：

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/12/14 下午1:38
#   Desc    :   Gitlab 备份脚本
import os
import time
import logging
import subprocess
from datetime import datetime
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(os.path.dirname(__file__), 'gitlab_backup_log.txt'),
    filemode='a',
    format='%(name)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
)
logger = logging.getLogger('Gitlab-backup')  # 设置log名称

BACKUP_DIR = '/mnt/test_gitlab_backup'
INSTALL_DIR = '/home/xueweihan/gitlab_xxx'


def backup():
    logger.info('begin script')
    now_datetime_str = datetime.now().strftime('%Y%m%d_%H_%M_%S')

    # 备份是必须关服务，否则会提示：‘redis.sock: socket ignored’等，socket 占用的问题
    # stop gitlab srevice
    os.system('{install_dir}/ctlscript.sh stop>> {backup_dir}/'
              '{time}-gitlab_backup.log2>&1'.format(install_dir=INSTALL_DIR,
              time=now_datetime_str,
              backup_dir=BACKUP_DIR))
    logger.info('gitlab service stop')
    time.sleep(10)

    command = 'cd {backup_dir} && tar -pczvf {time}-gitlab-backup.tar.gz {install_dir}>>' \
              '{backup_dir}/{time}-gitlab_backup.log2>&1'.format(backup_dir=BACKUP_DIR,
              time=now_datetime_str,
              install_dir=INSTALL_DIR)

    # backup
    logger.info('begin backup')
    os.system(command)
    time.sleep(10)
    logger.info('end backup')

    # 不论上面是否成功，都会执行下面的shell，因为不管备份成不成功都需要启动gitlab服务
    # start gitlab service
    os.system('{install_dir}/ctlscript.sh start>> {backup_dir}/'
              '{time}-gitlab_backup.log2>&1'.format(install_dir=INSTALL_DIR,
                           time=now_datetime_str,
                           backup_dir=BACKUP_DIR))
    logger.info('gitlab service start')

    logger.info('end script')


if __name__ == '__main__':
    try:
        backup()
    except Exception as e:
        logger.error(e)
```

```python
# 这段代码没用，用作后面备忘
# subprocess输出执行脚本过程的详细信息函数
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break

for line in runProcess('mysqladmin create test -uroot -pmysqladmin12'.split()):
    print line,
```

## crontab 配置
设定为每周日凌晨3点，跑备份脚本，设置 crontab ：`sudo crontab -u root -e`

```
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
# m h  dom mon dow   command
0 2 * * 0 python /home/xueweihan/gitlab_backup_script.py
```

### 在cron的实际使用过程中，你会遇到很多问题：
1、开启cron日志机制，过程是：
1. `sudo vi /etc/rsyslog.d/50-default.conf`

2. `#cron.*    /var/log/cron.log //去掉#，开启log机制`

3. `sudo service rsyslog restart`
4. `sudo service cron restart`


2、`/var/log/cron.log:Jun  8 14:48:01 ubuntu CRON[5706]: (CRON) info (No MTA installed, discarding output)`

解释如下：

```
  Linux uses mail for sending notifications to the user. Most linux distributions have an mail service (including an mta) installed.
　Ubuntu not.think your webserver program created its own cronjob due the installation process for sending notifications via mail. You can install a mail service, postfix for example, to solve this problem.

 这一段话的大致意思是说，crontab执行脚本时是不会直接错误的信息输出，而是会以邮件的形式发送到你的邮箱里，这时候就需要邮件服务器了，如果你没有安装邮件服务器，它就会报这个错。如果是测试，可以用下面的办法来解决：
　　This happens because your cron jobs are producing output and then the cron daemon tries to email that output to you (i.e. root). If you don't need that output, the easiest way to solve this is to discard it at the crontab:

　　$ sudo crontab -e

　　and add ">/dev/null 2>&1" (without quotes) to every job
```
