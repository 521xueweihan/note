## 起因
本期的[Python Weekly](http://www.pythonweekly.com/)，在邮件的最后一个“PyWeek 22 challenge”，我就好奇的点进去了，地址：https://pyweek.org/。

>The PyWeek challenge:
1. Invites entrants to write a game in one week from scratch either as an individual or in a team,
2. Is intended to be challenging and fun,
3. Will hopefully increase the public body of game tools, code and expertise,
4. Will let a lot of people actually finish a game, and
5. May inspire new projects (with ready made teams!)

就是一个python的挑战赛：用python写一个游戏，可以是个人参加也可以组队参加。然后，下面列出了挑战赛的时间表，要参加的同学自己研究下：
![]()

## 游戏
网站两个tab：Games和Previous Challenges里面列出了之前参赛的作品，每个游戏包含源码、评价和游戏截图。
Games：历史评分排行榜
![]()

Previous Challenges：之前获奖的作品，分个人和团队两项。
![]()

## 下载个玩一玩
下载个玩玩：我选了的是个人作品——[Beam](https://pyweek.org/e/Tee-py21/)——[下载地址](https://pyweek.org/media/dl/21/Tee-py21/Beam.zip)，游戏截图：
![]()

下载完，先看`README`，所有负责任的开源项目，都会在README中写依赖什么库，怎么运行等。README中提示`python run_game.py`运行游戏，但是执行的时候提示：`ImportError: No module named pygame`，原来是依赖pygame的库，执行命令`pip install pygame`(安装第三方库的时候，最好新建一个虚拟环境)。安装完后，再跑一下run_game脚本。运行成功：
![]()

玩了一会，熟悉了规则：
1. x键为加速，碰到‘激光’就Game Over，处于非加速状态有‘防护罩’不怕激光，
2. 两个以上‘激光柱’在一条线上，会发射激光
3. 机器人的屁股后面有个‘巨型激光追’
4. 成功的到达对面，侧为过关

所以就是通过x键，不被后面的激光追上，同时躲避路上的激光（非加速状态则可通过路上的激光扫射）。

## 运行游戏遇到的问题
#### 最好不要试玩太老的游戏
每个游戏都标记着上传的时间，有的游戏太老了，最好就不要下仔试玩了。因为，随着库的升级，运行的时候有可能会有问题。

#### mac下运行，错误提示：Python pygame error : Failed loading libpng.dylib: dlopen(libpng.dylib, 2): image not found
解决办法：`brew install libpng`

## 源码
整个游戏的代码，所有代码加起来不超过500百行。看来python写个简单的游戏，很便捷。主要代码在‘gamelib/game’文件中。主要分为一下几个类：
![]()

我忘记在哪里看过：熟悉代码的时候，一定要动手，不知道怎么动？1.随便改，改坏了，说明你上道了。 2.修好了，哎呦不错哦，懂了一些。

## 改
我想让机器人可以上下移动：

## 最后
