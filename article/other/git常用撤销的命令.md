## 基本概念
1. 工作区
2. 暂存区
3. 本地版本仓库
4. 远程版本仓库

如果不清晰上面的四个概念，请查看[廖老师的git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013745374151782eb658c5a5ca454eaa451661275886c6000)

这里我多说几句：最开始我使用git的时候，我并不明白我为什么写完代码要用git的一些列指令把我的修改
存起来。后来用多了，也就明白了为什么。git是一个“版本管理工具”，大家在写东西的时候都用过“回撤”
这个功能，但是回撤只能回撤几步，假如想要找回我三天之前的修改，光用“回撤”是找不回来的。而“版本管理工具”
就是记录每次的修改，只要提交到版本仓库，你就可以找到之前任何时刻的状态（文本状态）。

当然，上面我只说了一部分git的好处，只为后面的东西作为铺垫。因为，后面会说到三个关于git上面如何“反悔”、
“回到任意时候的代码”，其实就是上面说的原始的“回撤”升级版，版本管理工具的“回撤”。


## checkout、reset、revert这三个指令
- checkout：清空工作区的修改
	- 清空`工作区`的修改`git checkout changed_file`，清空所有`工作区`的修改`git checkout .`
	- 切换分支`git checkout branch_name`(在切换分支之前，需要清空工作区，提交到`本地版本仓库`或者`移除工作区的东西`)
	- 快速查看某个版本的代码`git checkout commit_id/HEAD~last_version_num`，切换到一个临时分支，内容就是指定的版本内容

- reset：撤销某次提交(commit)，并把这次提交的所有修改放到工作区
	- `git reset HEAD~last_version_num/commit_id`，注意：这个操作修改历史，所以push到
	远程仓库会出现问题，可以通过`-f`参数，实现强制推送。

- revert：回到之前的某个版本的状态，并创建一个新的提交。
	- `git revert HEAD~last_version_num/commit_id`，创建一个新的commit，该内容为指定的
	版本的内容，注意：这个操作并不会重写历史，也就是原来的commit还是存在的。

git reset 和git revert的区别：  
git revert是用一次新的commit来回滚之前的commit，git reset是直接删除指定的commit。  
git reset 是把HEAD向后移动了一下，而git revert是HEAD继续前进  

在回滚这一操作上看，虽然效果差不多，但是日后继续merge以前的老版本时有区别。因为git revert是用一次逆向的commit“中和”之前的提交，因此日后合并老的branch时，导致这部分改变不会再次出现，但是git reset是之间把某些commit在某个branch上删除，因而和老的branch再次merge时，这些被回滚的commit应该还会被引入。

## 参考
- [廖雪峰git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374831943254ee90db11b13d4ba9a73b9047f4fb968d000)
- [maiyang](http://maiyang.github.io/git/2016/04/21/git-reset-checkout-revert)
