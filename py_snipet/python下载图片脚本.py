#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/3/9 下午4:16
#   Desc    :   下载图片脚本

import requests

PATH = '/Users/sx/Downloads/img'   #保存图片的路径

# 图片的url
URLS = [
'[pic1]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165053600-1959617063.png "回旋镖"',
'[pic2]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165138632-1466995563.png "即兴表演"',
'[pic3]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165207460-1663227069.png "html游戏"',
'[pic4]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165245585-13132324.png "SICP"',
'[pic5]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165316054-508078873.png "little printf"',
'[pic6]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165345132-240153505.png "系统结构图1"',
'[pic7]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165410819-912010443.png "系统结构图2"',
'[pic8]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165434038-1047419834.png "enjoy!"',
'[pic9]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165509288-362105815.png "一团糟"',
'[pic10]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165553491-1103998786.png "建筑"',
'[pic11]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165619132-1692419680.png "骄傲的高级工程师"',
'[pic12]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165643475-167381198.png "第五章周围都是书的程序员"',
'[pic13]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165721179-136562872.png "第六章忘记吃午饭的程序员"',
'[pic14]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165756069-1874490817.png "progamming is shit"',
'[pic15]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165828116-1711952615.png "第七章盲目追求框架的程序员"',
'[pic16]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165915194-205136211.png "第八章疲惫不堪的女程序员"',
'[pic17]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309165941944-768486562.png "第九章架构师"',
'[pic18]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309170007475-1012911461.png "第十章"',
'[pic19]: http://images2015.cnblogs.com/blog/759200/201603/759200-20160309170050850-176160102.png "第十一章"'
]


class Img(object):
    def __init__(self, url):
        self.file_name = url.split('/')[-1]
        self.url = url
        self.path = PATH+'/'+self.file_name

    @property
    def data(self):
        r = requests.get(self.url)
        return r.content

    def save(self):
        with open(self.path, 'wb') as fb:
            fb.write(self.data)

for i, url in enumerate(URLS):
    url = url.split(' ')[1]
    Img(url).save()
    print u'第{}／共{}：{}'.format(i+1, len(URLS), 'sucess')
