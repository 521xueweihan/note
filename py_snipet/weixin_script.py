#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/9/14 下午4:00
#   Desc    :   微信发消息脚本
from __future__ import print_function

import os
import requests
import re
import time
import xml.dom.minidom
import json
import sys
import math
import subprocess
import ssl
import threading

DEBUG = False

MAX_GROUP_NUM = 2  # 每组人数
INTERFACE_CALLING_INTERVAL = 5  # 接口调用时间间隔, 间隔太短容易出现"操作太频繁", 会被限制操作半小时左右
MAX_PROGRESS_LEN = 50

QRImagePath = os.path.join(os.getcwd(), 'qrcode.jpg')

tip = 0
uuid = ''

base_uri = ''
redirect_uri = ''
push_uri = ''

skey = ''
wxsid = ''
wxuin = ''
pass_ticket = ''
deviceId = 'e000000000000000'

BaseRequest = {}

ContactList = []
My = []
SyncKey = []

try:
    xrange
    range = xrange
except:
    # python 3
    pass


def responseState(func, BaseResponse):
    ErrMsg = BaseResponse['ErrMsg']
    Ret = BaseResponse['Ret']
    if DEBUG or Ret != 0:
        print('func: %s, Ret: %d, ErrMsg: %s' % (func, Ret, ErrMsg))

    if Ret != 0:
        return False

    return True



def getUUID():
    global uuid

    url = 'https://login.weixin.qq.com/jslogin'
    params = {
        'appid': 'wx782c26e4c19acffb',
        'fun': 'new',
        'lang': 'zh_CN',
        '_': int(time.time()),
    }

    r= myRequests.get(url=url, params=params)
    r.encoding = 'utf-8'
    data = r.text

    # print(data)

    # window.QRLogin.code = 200; window.QRLogin.uuid = "oZwt_bFfRg==";
    regx = r'window.QRLogin.code = (\d+); window.QRLogin.uuid = "(\S+?)"'
    pm = re.search(regx, data)

    code = pm.group(1)
    uuid = pm.group(2)

    if code == '200':
        return True

    return False


def showQRImage():
    global tip

    url = 'https://login.weixin.qq.com/qrcode/' + uuid
    params = {
        't': 'webwx',
        '_': int(time.time()),
    }

    r = myRequests.get(url=url, params=params)

    tip = 1

    f = open(QRImagePath, 'wb')
    f.write(r.content)
    f.close()
    time.sleep(1)

    if sys.platform.find('darwin') >= 0:
        subprocess.call(['open', QRImagePath])
    elif sys.platform.find('linux') >= 0:
        subprocess.call(['xdg-open', QRImagePath])
    else:
        os.startfile(QRImagePath)

    print('请使用微信扫描二维码以登录')


def waitForLogin():
    global tip, base_uri, redirect_uri, push_uri

    url = 'https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s' % (
        tip, uuid, int(time.time()))

    r = myRequests.get(url=url)
    r.encoding = 'utf-8'
    data = r.text

    # print(data)

    # window.code=500;
    regx = r'window.code=(\d+);'
    pm = re.search(regx, data)

    code = pm.group(1)

    if code == '201':  # 已扫描
        print('成功扫描,请在手机上点击确认以登录')
        tip = 0
    elif code == '200':  # 已登录
        print('正在登录...')
        regx = r'window.redirect_uri="(\S+?)";'
        pm = re.search(regx, data)
        redirect_uri = pm.group(1) + '&fun=new'
        base_uri = redirect_uri[:redirect_uri.rfind('/')]

        # push_uri与base_uri对应关系(排名分先后)(就是这么奇葩..)
        services = [
            ('wx2.qq.com', 'webpush2.weixin.qq.com'),
            ('qq.com', 'webpush.weixin.qq.com'),
            ('web1.wechat.com', 'webpush1.wechat.com'),
            ('web2.wechat.com', 'webpush2.wechat.com'),
            ('wechat.com', 'webpush.wechat.com'),
            ('web1.wechatapp.com', 'webpush1.wechatapp.com'),
        ]
        push_uri = base_uri
        for (searchUrl, pushUrl) in services:
            if base_uri.find(searchUrl) >= 0:
                push_uri = 'https://%s/cgi-bin/mmwebwx-bin' % pushUrl
                break

        # closeQRImage
        if sys.platform.find('darwin') >= 0:  # for OSX with Preview
            os.system("osascript -e 'quit app \"Preview\"'")
    elif code == '408':  # 超时
        pass
    # elif code == '400' or code == '500':

    return code


def login():
    global skey, wxsid, wxuin, pass_ticket, BaseRequest

    r = myRequests.get(url=redirect_uri)
    r.encoding = 'utf-8'
    data = r.text

    # print(data)

    doc = xml.dom.minidom.parseString(data)
    root = doc.documentElement

    for node in root.childNodes:
        if node.nodeName == 'skey':
            skey = node.childNodes[0].data
        elif node.nodeName == 'wxsid':
            wxsid = node.childNodes[0].data
        elif node.nodeName == 'wxuin':
            wxuin = node.childNodes[0].data
        elif node.nodeName == 'pass_ticket':
            pass_ticket = node.childNodes[0].data

    # print('skey: %s, wxsid: %s, wxuin: %s, pass_ticket: %s' % (skey, wxsid,
    # wxuin, pass_ticket))

    if not all((skey, wxsid, wxuin, pass_ticket)):
        return False

    BaseRequest = {
        'Uin': int(wxuin),
        'Sid': wxsid,
        'Skey': skey,
        'DeviceID': deviceId,
    }

    return True


def webwxinit():

    url = (base_uri +
        '/webwxinit?pass_ticket=%s&skey=%s&r=%s' % (
            pass_ticket, skey, int(time.time())) )
    params  = {'BaseRequest': BaseRequest }
    headers = {'content-type': 'application/json; charset=UTF-8'}

    r = myRequests.post(url=url, data=json.dumps(params),headers=headers)
    r.encoding = 'utf-8'
    data = r.json()

    if DEBUG:
        f = open(os.path.join(os.getcwd(), 'webwxinit.json'), 'wb')
        f.write(r.content)
        f.close()


    # print(data)

    global ContactList, My, SyncKey
    dic = data
    ContactList = dic['ContactList']
    My = dic['User']
    SyncKey = dic['SyncKey']

    state = responseState('webwxinit', dic['BaseResponse'])
    return state


def webwxgetcontact():

    url = (base_uri +
        '/webwxgetcontact?pass_ticket=%s&skey=%s&r=%s' % (
            pass_ticket, skey, int(time.time())) )
    headers = {'content-type': 'application/json; charset=UTF-8'}


    r = myRequests.post(url=url,headers=headers)
    r.encoding = 'utf-8'
    data = r.json()

    if DEBUG:
        f = open(os.path.join(os.getcwd(), 'webwxgetcontact.json'), 'wb')
        f.write(r.content)
        f.close()

    # print(data)

    dic = data
    MemberList = dic['MemberList']

    # 倒序遍历,不然删除的时候出问题..
    SpecialUsers = [
        "newsapp", "fmessage", "filehelper", "weibo", "qqmail", "tmessage",
        "qmessage", "qqsync", "floatbottle", "lbsapp", "shakeapp", "medianote",
        "qqfriend", "readerapp", "blogapp", "facebookapp", "masssendapp",
        "meishiapp", "feedsapp", "voip", "blogappweixin", "weixin",
        "brandsessionholder", "weixinreminder", "wxid_novlwrv3lqwv11",
        "gh_22b87fa7cb3c", "officialaccounts", "notification_messages",
        "wxitil", "userexperience_alarm"]
    for i in range(len(MemberList) - 1, -1, -1):
        Member = MemberList[i]
        if Member['VerifyFlag'] & 8 != 0:  # 公众号/服务号
            MemberList.remove(Member)
        elif Member['UserName'] in SpecialUsers:  # 特殊账号
            MemberList.remove(Member)
        elif Member['UserName'].find('@@') != -1:  # 群聊
            MemberList.remove(Member)
        elif Member['UserName'] == My['UserName']:  # 自己
            MemberList.remove(Member)

    return MemberList


def syncKey():
    SyncKeyItems = ['%s_%s' % (item['Key'], item['Val'])
                    for item in SyncKey['List']]
    SyncKeyStr = '|'.join(SyncKeyItems)
    return SyncKeyStr


def syncCheck():
    url = push_uri + '/synccheck?'
    params = {
        'skey': BaseRequest['Skey'],
        'sid': BaseRequest['Sid'],
        'uin': BaseRequest['Uin'],
        'deviceId': BaseRequest['DeviceID'],
        'synckey': syncKey(),
        'r': int(time.time()),
    }

    r = myRequests.get(url=url,params=params)
    r.encoding = 'utf-8'
    data = r.text

    # print(data)

    # window.synccheck={retcode:"0",selector:"2"}
    regx = r'window.synccheck={retcode:"(\d+)",selector:"(\d+)"}'
    pm = re.search(regx, data)

    retcode = pm.group(1)
    selector = pm.group(2)

    return selector


def webwxsync():
    global SyncKey

    url = base_uri + '/webwxsync?lang=zh_CN&skey=%s&sid=%s&pass_ticket=%s' % (
        BaseRequest['Skey'], BaseRequest['Sid'], pass_ticket)
    params = {
        'BaseRequest': BaseRequest,
        'SyncKey': SyncKey,
        'rr': ~int(time.time()),
    }
    headers = {'content-type': 'application/json; charset=UTF-8'}

    r = myRequests.post(url=url, data=json.dumps(params))
    r.encoding = 'utf-8'
    data = r.json()

    # print(data)

    dic = data
    SyncKey = dic['SyncKey']

    state = responseState('webwxsync', dic['BaseResponse'])
    return state


def heartBeatLoop():
    while True:
        selector = syncCheck()
        if selector != '0':
            webwxsync()
        time.sleep(1)


def _transcoding(data):
    if not data:
        return data
    result = None
    if type(data) == unicode:
        result = data
    elif type(data) == str:
        result = data.decode('utf-8')
    return result


def auto_send_msg(receiver):

    choose = input(u'\n选择发送信息的内容：\n1.home 下班\n2.overtime 加班\n3.dinner 回去吃\n>'.encode('utf-8'))
    choose_map = {1: u'已经下班，在回家的路上。', 2: u'今天加班！下班没谱了。', 3: u'今天早下班，晚饭回去吃。'}
    content = u"Hi，{receiver_nickname} ： \n我{msg} " \
              u"\n\n这条信息是通过脚本发送，请勿回复～".\
        format(receiver_nickname=receiver, msg=choose_map[choose])

    member_list = webwxgetcontact()
    for fi_member in member_list:
        if fi_member.get('RemarkName', ''):
            if fi_member.get('RemarkName') == receiver:
                return send_message(fi_member, content)

    print(u'根据备注，未找到接收消息的人')


def send_message(receiver_info, content):
    msg = {
            'ClientMsgId': str(int(time.time() * 1000000)),
            'Content': _transcoding(content),
            'FromUserName': My['UserName'],
            'LocalID': str(int(time.time() * 1000000)),
            'ToUserName': receiver_info['UserName'],
            'Type': 1
        }
    url = (base_uri + '/webwxsendmsg?pass_ticket=%s' % pass_ticket)
    params = {
        'BaseRequest': BaseRequest,
        'Msg': msg,
        'Scene': 0,
    }
    headers = {'content-type': 'application/json; charset=UTF-8'}
    data = json.dumps(params, ensure_ascii=False).encode('utf-8')
    r = myRequests.post(url=url, data=data, headers=headers)
    result = r.json()
    return result['BaseResponse']['Ret'] == 0


def main():
    global myRequests

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '44.0.2403.125 Safari/537.36'}
    myRequests = requests.Session()
    myRequests.headers.update(headers)

    if not getUUID():
        print('获取uuid失败')
        return

    print('正在获取二维码图片...')
    showQRImage()

    while waitForLogin() != '200':
        pass

    os.remove(QRImagePath)

    if not login():
        print('登录失败')
        return

    if not webwxinit():
        print('初始化失败')
        return

    print('开启心跳线程')
    threading.Thread(target=heartBeatLoop)

    print('---------------------------------------------')
    if auto_send_msg(u'xxx'):
        print('Send msg: Successful!')
    else:
        print('Send msg: Error~')
    print('---------------------------------------------')

# windows下编码问题修复
# http://blog.csdn.net/heyuxuanzee/article/details/8442718

class UnicodeStreamFilter:

    def __init__(self, target):
        self.target = target
        self.encoding = 'utf-8'
        self.errors = 'replace'
        self.encode_to = self.target.encoding

    def write(self, s):
        if type(s) == str:
            try:
                s = s.decode('utf-8')
            except:
                pass
        s = s.encode(self.encode_to, self.errors).decode(self.encode_to)
        self.target.write(s)

if sys.stdout.encoding == 'cp936':
    sys.stdout = UnicodeStreamFilter(sys.stdout)

if __name__ == '__main__':

    print('微信脚本')
    main()
    print('退出...')
