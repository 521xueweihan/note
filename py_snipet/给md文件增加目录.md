#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/7/22 下午6:23
#   Desc    :   给md文档加可跳转目录

PATH = ''

style = '* [Everyday Git in twenty commands or so](#everyday-git-in-twenty-commands-or-so)'


def process_content(content):
    href_list = []

    for i, fi_content in enumerate(content):
        if fi_content.startswith('## '):
            href_name = fi_content.split('## ')[1][:-1]
            href_content = '* [{name}](#{name})'.format(name=href_name)
            print href_content
            href_list.append(href_content)
    return href_list


def read_file(path):
    with open(path, 'r+') as fb:
        href_list = process_content(fb.readlines())


read_file(PATH)
