
#### 美化完的格式：

`git log --graph --pretty=format:'%C(yellow)%h%Creset -%C(cyan)%d%Creset %s %Cgreen(%an, %cr)' --abbrev-commit`

#### 写入 ~/.gitconfig 中：

`git config --global alias.ll "log --graph --pretty=format:'%C(yellow)%h%Creset -%C(cyan)%d%Creset %s %Cgreen(%an, %cr)' --abbrev-commit"`

通过`git ll`查看，之前没有记录`git log`参数信息，这里记录下，免得后面再重新查找

| 参数     | 说明     |
| :------------- | :------------- |
| %H	| commit hash |
| %h	| commit short hash |
| %T	|tree hash |
| %t	|tree short hash |
| %P	|parent hash |
| %p	|parent short hash|
|%an	|作者名字|
|%aN	|.mailmap 中对应的作者名字|
|%ae	|作者邮箱|
|%aE	|.mailmap 中对应的作者邮箱|
|%ad	|–date=制定的日期格式|
|%aD	|RFC2822 日期格式|
|%ar	|日期格式，例如：1 day ago|
|%at	|UNIX timestamp 日期格式|
|%ai	|ISO 8601 日期格式|
|%cn	|提交者名字|
|%cN	|.mailmap 对应的提交的名字|
|%ce	|提交者邮箱|
|%cE	|.mailmap 对应的提交者的邮箱|
|%cd	|–data=制定的提交日期的格式|
|%cD	|RFC2822 提交日期的格式|
|%cr	|提交日期的格式，例如：1day ago|
|%ct	|UNIX timestamp 提交日期的格式|
|%ci	|ISO 8601 提交日期的格式|
|%d	|ref 名称|
|%e	|encoding|
|%s	|commit 信息标题|
|%f	|过滤 commit 信息的标题使之可以作为文件名|
|%b	|commit 信息内容|
|%N	|commit notes|
|%gD	|reflog selector, e.g., refs/stash@{1}|
|%gd	|shortened reflog selector, e.g., stash@{1}|
|%gs	|reflog subject|
|%Cred	|切换至红色|
|%Cgreen	|切换至绿色|
|%Cblue	|切换至蓝色|
|%Creset	|重设颜色|
|%C(color)	|制定颜色，as described in color.branch.* config option|
|%m	|left right or boundary mark|
|%n	|换行|
|%%	a |raw %|
|%x00	|print a byte from a hex code|
|%w([[,[,]]])	|switch line wrapping, like the -w option of git-shortlog(1).|
