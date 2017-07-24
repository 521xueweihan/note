# 让 Python 带你进入开源的世界——Git 从入门到与他人协作开发
我认为开源社区中有很多优秀的资源，并且可以帮助进阶中的程序员提高编程能力和水平。所以，我发起了[《HelloGitHub》月刊](https://hellogithub.com)，同时开始编写《让 Python 带你进入开源的世界》系列，希望更多的小伙伴加入到开源的社区当中。我个人能力有限，分享的知识都是通过我认真的收集、整理、总结、编写，那就欢迎持续关注，并加入到其中 😁。下面就是正文了：

本篇分为三个阶段：领进门（新手）、搜肠刮肚的建议（进阶）、后续的个人修行，所以可以根据自身情况通过下面的目录进行选阶段阅读。

**建议：** 如果是新手的话，请依次完成每一部分的实践通过后，再学习下一部分。

## 目录
- [Git 入门](#1)
    - [Git 和 GitHub 的关系](#1-1)
    - [实践](#1-2)
- [Git 基本使用规范](#2)
- [Git 工作流](#3)
    - [Git 工作流1（非项目内成员）](#3-1)：多用于为 GitHub 上的开源项目贡献代码
    - [Git 工作流2（项目内成员）](#3-2)：常用用于工作中
    - [编写优秀的 commit 信息](#3-3)
    - [实践](#3-4)
- [更多 Git 使用技巧](#4)
- [建议收集](#5)
- [参考](#6)

<a name="1"></a>
## 1. Git 入门
Git 是一个“分布式版本管理工具”，简单的理解版本管理工具：大家在写东西的时候都用过“回撤”这个功能，但是回撤只能回撤几步，假如想要找回我三天之前的修改，光用“回撤”是找不回来的。而“版本管理工具”能记录每次的修改，只要提交到版本仓库，你就可以找到之前任何时刻的状态（文本状态）。

<a name="1-1"></a>
### 1.1 Git 和 GitHub 的关系
Git 是一个“分布式版本管理工具”，这里需要理解分布式。也就是每个用户会有一个本地仓库，同时还有一个远程仓库。而 **GitHub 就是用户远程仓库的托管网站**。不同用户可以复制同一个仓库的代码到本地，然后开发某一部分功能，完成后提交请求到远程仓库。如果合并成功，后面用户再获取、更新该远程仓库的代码，就会包含你开发的功能，从而达到多个用户同时开发不同模块互不影响的效果。

例如：Gitlab、Bitbucket、自搭建的 Git 服务器等，都是同样的道理。

由于篇幅问题，我把 **GitHub 入门** 部分提前写出来了，可以在后面的实践部分阅读。

<a name="1-2"></a>
### 1.2 实践
参考我写的 **GitHub 入门教程**，还有我推荐的 **Git 极简入门教程**
1. [GitHub 入门教程](http://www.cnblogs.com/xueweihan/p/7217846.html)：先创建账号，到第四步在参考下面的教程。
2. [Git 极简入门教程](http://rogerdudler.github.io/git-guide/index.zh.html)：在上述教程中创建的项目中，练习本教程中的命令，并理解其作用。

**练习：**

1. 请跟着 **GitHub 入门教程** 的步骤，创建项目并提交修改。
2. 阅读 **Git 极简入门教程**，创建一个任意分支，并推送到远程仓库。
最后，[点击这里](https://github.com/521xueweihan/test_project/issues/new)，提交你创建的项目地址。

我会及时给出回复。如果完成了上述步骤并通过，你就可以阅读下面的章节了。

<a name="2"></a>
## 2. 基本规范
> 本部分翻译修改自：[project-guidelines](https://github.com/wearehive/project-guidelines)

首先，不管是项目的**管理者**或**贡献者**，都需要了解的一些基本规则：

* 从 `develop` 分支创建新的分支

    _原因：_
    > 这样可以确保 master 分支总是没有问题的，从而可以直接运行或者发布。同时因为 develop 分支是开发的主分支，可以确保所有子分支都是继承于同一分支开发。

* 创建 `feature` 分支开发新的功能

    _原因：_
    > 因为这样所有的工作都是在专用分支（feature）而不是主分支上，使得彼此的工作是完全隔离的。它允许你随意提交请求而不会影响其他人的开发。你可以实时迭代你开发的功能，即使这些代码是未完成，也不会污染和影响公共分支。

* 通过 Pull Request 方式提交代码到 `develop` 或 `master`，不要直接 Push

    _原因：_
    > 因为 PR 的方式可以通知所有团队成员你已完成该模块的功能，还可以轻松地对代码进 Review，并可以在该 PR 下讨论功能和交流。

* 同步本地的 `develop` 分支到最新，然后通过 `rebase` 命令合并到你的 `feature` 分支，最后提交 PR

    _原因：_
    > 因为，在 `feature` 分支上，通过 rebase 命令合并 `develop` 分支是不会产生额外的 commit（假设没有冲突），从而可以得到一个干净整洁的提交历史。

* 先通过 rebase 命令解决冲突，然后再提交 Pull Request
* 提交通过后删除本地和远程的 `feature` 分支（项目内成员）

    _原因：_
    > 因为，分支过多会造成不必要的混乱和重复提交，要记住 feature 分支只存在于开发进行时。

* 在提交 Pull Request 之前，确保你的分支代码运行没问题并且通过测试（包括代码风格检测）

    _原因：_
    > 你将要提交代码到稳定的分支，如果你的功能分支测试失败，那么同样的会导致目标分支运行、测试失败。与此同时，PR 之前你还需要检测代码是否有代码风格检测，这样做的目的是为了让整个项目的代码更加易读、统一。

* 记得设置 `.gitignore` 文件

    _原因：_
    > 有了 .gitignore 文件，就可以把运行过程中或者 ide 产生的并不是项目本身的文件过滤掉。

* 把 `develop` 和 `master` 分支设置为保护

    _原因：_
    > 它保护你的生产和开发分支免受意外和不可挽回的错误。更多现详情可以阅读，[GitHub 关于 protected 的说明](https://help.github.com/articles/about-protected-branches/)

<a name="3"></a>
## 3. Git 工作流

工作流分为：
1. 工作流1（非项目内成员）：未被邀请进项目，也就无法直接创建分支
2. 工作流2（项目内成员）：已经被邀请进项目，可以直接创建分支

GitHub 上为开源项目提交代码就用：**非项目内成员工作流**

工作中大多使用：**项目内成员工作流**

两种工作流，相差的并不多，推荐先学习 **工作流1**。

<a name="3-1"></a>
### 3.1 Git 工作流1（非项目内成员）
因为不是项目中的成员，无法直接修改项目中的代码。所以需要先拷贝（Fork）项目到自己的远程仓库中（GitHub账号下），然后基于自己克隆过来的项目开发新的功能，最后提交 PR。

**project_url**：想要贡献代码的项目地址（源地址）  
**fork_project_url**：克隆到自己远程仓库的项目地址

* Fork 项目
    ```sh
    项目首页 "Fork"
    ```
* 下载项目
    ```sh
    git clone fork_project_url
    ```
* 增加源项目仓库地址
    ```sh
    git remote add <origin-name> project_url
    ```
* 切换到 `develop` 分支
    ```sh
    git checkout develop
    ```
* 创建新的 feature或bug-fix 分支
    ```sh
    git checkout -b <branchname>
    ```
* 保存你的修改（开发、修复bug）
    ```sh
    git add
    git commit -a
    ```
    _原因：_
    > `git commit -a` 命令中的 `-a` 参数是开启编辑器编辑 commit 信息，会在后面有详细的说明。

* 更新到与远程仓库同步
    ```sh
    git checkout develop
    git pull --rebase <origin-name> develop
    ```
* 把最新的 develop 分支通过 rebase 命令合并到 feature 分支和对应的远程分支
    ```sh
    git checkout <branchname>
    git rebase -i --autosquash develop
    ```

    _原因：_
    > 你可以通过 `--autosquash` 命令把多个 commit 压缩成一个 commit，这样是的历史更加整洁，一个功能就一个commit。通过 rebase 在本地就把冲突解决好，以避免提交 PR 时才发现冲突，导致提交失败。

* 如果在合并时没有出现冲突（conflict）就跳过这步；如果有冲突，可以先修改文件中的冲突，然后执行下面的命令。
    ```sh
	git add <file1> <file2> ...
    git rebase --continue
    ```
* Rebase 命令会修改历史，所以你 push 时可能会需要加上 `-f` 强制修改历史。如果有其他人也在你的分支上开发，就使用 `--force-with-lease` 减少破坏
    ```sh
    git push -f
    ```

    _原因：_
    > 因为只是修改 feature 分支的历史，而且每个 feature 是独立（理论上只有一个人开发），所以在 push 时加上 -f 参数并不会影响其他人的工作。

* 提交 Pull Request
* Pull request 被接受、合并完成，就关闭该评论
* 如上述步骤都已完成，删除你本地和远程的 feature 分支
  ```sh
  git branch -d <branchname>
  git push origin --delete <remote-branchname>
  ```

<a name="3-2"></a>
### 3.2 Git 工作流2（项目内成员）
这种工作流，更适合用在工作中。

* 下载项目
    ```sh
    git clone project_url
    ```
* 切换到 `develop` 分支
    ```sh
    git checkout develop
    ```
* 创建新的 feature或bug-fix 分支
    ```sh
    git checkout -b <branchname>
    ```
* 保存你的修改（开发、修复bug）
    ```sh
    git add
    git commit -a
    ```
    _原因：_
    > `git commit -a` 命令中的 `-a` 参数是开启编辑器（[vim基本操作](http://www.cnblogs.com/xueweihan/p/5737962.html)）编辑 commit 信息，会在后面有详细的说明。

* 更新到与远程仓库同步
    ```sh
    git checkout develop
    git pull --rebase
    ```
* 把最新的 develop 分支通过 rebase 命令合并到 feature 分支和对应的远程分支
    ```sh
    git checkout <branchname>
    git rebase -i --autosquash develop
    ```

    _原因：_
    > 你可以通过 `--autosquash` 命令把多个 commit 压缩成一个 commit，这样是的历史更加整洁，一个功能就一个commit。通过 rebase 在本地就把冲突解决好，以避免提交 PR 时才发现冲突，导致提交失败。

* 如果在合并时没有出现冲突（conflict）就跳过这步；如果有冲突，可以修改文件中的冲突，然后执行下面的命令。
    ```sh
    git add <file1> <file2> ...
    git rebase --continue
    ```
* Rebase 命令会修改历史，所以你 push 时可能会需要加上 `-f` 强制修改历史。如果有其他人也在你的分支上开发，就使用 `--force-with-lease` 减少破坏
    ```sh
    git push -f
    ```

    _原因：_
    > 因为只是修改 feature 分支的历史，而且每个 feature 是独立（理论上只有一个人开发），所以在 push 时加上 -f 参数并不会影响其他人的工作。

* 提交 Pull Request
* Pull request 被接受、合并完成，就关闭该评论
* 如上述步骤都已完成，删除你的本地 feature 分支
    ```sh
    git branch -d <branchname>
    git push origin --delete <remote-branchname>
    ```

<a name="3-3"></a>
### 3.3 编写优秀的 commit 信息
制定良好的创建 commit 规范，并坚持使用，使得与他人合作更容易。下面是一些经验和建议：

* 把 commit 信息分为 标题和内容两个部分，两者之间要有个空行

    _原因：_
    > Git 可将你的提交消息的第一行做为摘要

* 标题控制在 50 个字符以内，内容最多不超过 72 个字符

    _原因：_
    > commit 信息尽可能简洁和精准

* 标题首字母大写
* 标题不要有句号
* 标题使用“祈求语句”
* 内容中解释为什么要有这次提交、如何解决问题、可能影响的地方

    _原因：_
    > 如果有需求、issues地址、可以附上。[更多详情](https://ruby-china.org/topics/15737)

<a name="3-4"></a>
### 3.4 实践
本节就一个实践内容，但是并不是很简单，请仔细阅读并遵守：

向我的 test_project 项目的 develop 分支提交一个PR，要求如下：
1. 在 `README.md` 文件中新启一行，增加内容为上一个 commit 的 id 号
2. Commit 信息要按照上述 3.3 节要求书写

**提示：** 可能会因为接受提交顺序而产生冲突，如遇到冲突，要解决完冲突后重新提交。如遇问题，可参考 “4. 更多 Git 使用技巧”。


<a name="4"></a>
## 4. 更多 Git 使用技巧
>俗话说：师傅领进门修行靠个人。

用好一个工具或技能最好的方式就是不断的使用，使用中必然会出现问题。当你解决了足够多的问题，你也就成为老司机了。

遇到问题：
- 请先阅读错误提示
- 通过搜索引擎寻找答案（国内推荐使用 bing 搜索技术问题）
- 用自己的语言经可能详细的描述问题，并收集充足的信息后，在询问老司机

最后，请拿走这本秘籍：[git-tips](https://github.com/521xueweihan/git-tips)，😄

<a name="5"></a>
## 5. 建议收集
本教程肯定还有不足的地方或者你觉得好的地方，欢迎自由留言积极讨论，希望这个系列能够帮助到更多的小伙伴！

- 本教程不好的地方？
- 是否需要提供视频教程？
- 零基础入门是否感觉到吃力？

<a name="6"></a>
## 参考
- [project-guidelines](https://github.com/wearehive/project-guidelines)
- [autosquashing-git-commits](https://robots.thoughtbot.com/autosquashing-git-commits)
- [Git 写出好的 commit message](https://ruby-china.org/topics/15737)
