## git pull --rebase时产生冲突
有三个选项：
1. `git rebase --skip`
效果是：抛弃本地的commit，采用远程的commit

2. `git rebase --abort`
效果是：终止这次rebase

3. `git rebase --continue`
当你修改完冲突的文件：执行｀git add .｀，最后`git rebase --continue`就可以解决完冲突并合并到分支上了。就可以push了。
