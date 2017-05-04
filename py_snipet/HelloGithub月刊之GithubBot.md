## 起因
我在github上发起了一个开源项目：[《HelloGithub月刊》](https://github.com/521xueweihan/HelloGithub)，内容是github上收集的好玩，容易上手的开源项目。

目的：因为`兴趣是最好的老师`，我希望月刊中的内容可以激发读者的兴趣，从而动手参与到开源的项目中，一方面提高编程技术、另一方面哪怕是能力有限不能为开源项目提交代码，也可以给个‘star’，表示对有意思、优秀的开源项目的支持！从而让开源社区越来越好。

所以，我就需要收集github上的开源项目，目前通过两种方式发现github上优秀的项目：  
1. Follow活跃的Github用户，收集他们Starred的项目
2. Github的Explore页

然后，我就想能不能写个脚本，每天跑一次把这两个数据源的数据，收集整理好，然后发到我的邮箱中。这个需求很简单，初步感觉就两个问题：
1. 数据源的api
2. 发邮件的方法

## 过程
### 数据源
[Github API](https://developer.github.com/v3/)提供了诸多获取Github数据的接口：
1. [List public events that a user has received](https://developer.github.com/v3/activity/events/#list-public-events-that-a-user-has-received)：`GET /users/:username/received_events/public`，这个接口返回user的动态（包含user关注的用户、项目的动态）
2. 暂时没找到Explore页的接口，如果实在找不到，我就尝试爬取。

### 代码
**完整的代码**：[我的Github](https://github.com/521xueweihan/HelloGithub/tree/master/script)

##### 1、请求api：
首选requests库，真的是居家旅行必备良品。需要注意一点，请求`GET /users/:username/received_events/public`，**需要用户验证**，请求api的函数如下：
```python
def get_data(page=1, per_page=100):
    """
    从目标源获取数据
    """

    args = '?page={page}&per_page={per_page}'.format(
        page=page, per_page=per_page)

    response = requests.get(API['events']+args,
                            auth=(ACCOUNT['username'], ACCOUNT['password']))
    status_code = response.status_code
    if status_code == 200:
        resp_json = response.json()
        return resp_json
    else:
        logging.error('请求api失败：', status_code)
        return None
```

##### 2、根据条件过滤数据：
请求api回来的json数据如下：
```
[
	...
  {
    "id": "4123123423",
    "type": "WatchEvent",
    "actor": {
      "id": 12342134,
      "login": "gera2ld",
      "display_login": "gera2ld",
      "gravatar_id": "",
      "url": "https://api.github.com/users/gera2ld",
      "avatar_url": "https://avatars.githubusercontent.com/u/3139113?"
    },
    "repo": {
      "id": 23412431,
      "name": "yahoo/gifshot",
      "url": "https://api.github.com/repos/yahoo/gifshot"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2016-09-03T16:25:34Z",
    "org": {
      "id": 234234,
      "login": "yahoo",
      "gravatar_id": "",
      "url": "https://api.github.com/orgs/yahoo",
      "avatar_url": "https://avatars.githubusercontent.com/u/16574?"
    }
  },
  {
    "id": "234234",
    "type": "WatchEvent",
    "actor": {
      "id": 21341234,
      "login": "phith0n",
      "display_login": "phith0n",
      "gravatar_id": "",
      "url": "https://api.github.com/users/phith0n",
      "avatar_url": "https://avatars.githubusercontent.com/u/5711185?"
    },
    "repo": {
      "id": 23234,
      "name": "yummybian/ThreadPool",
      "url": "https://api.github.com/repos/yummybian/ThreadPool"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2016-09-03T16:12:56Z"
  }
]
	...
```
分析上面的json数据，其中可能会包含我不需要的信息（非starred事件的数据）需要过滤掉、同时需要根据时间获取某一段时间的数据。比如我写的这个github bot脚本获取24个小时的数据，我设定脚本每天凌晨4点跑——例如：9.3 4:00——9.4 4:00(24h的数据)。下面写了两个函数，用于过滤符合条件的数据：

**注意**: 接口返回的数据中的create_at字段的时间值形如——`created_at: "2016-09-03T16:12:56Z"
`是‘协调世界时’，‘Z’是协调世界时中0时区的标志，北京是8时区，所以就是需要在这个时间的基础上+8小时。这个事件发生于北京时间："2016-09-04 00:12:56"

```python
def check_condition(data):
    """
    过滤条件
    """
    create_time = datetime.datetime.strptime(
        data['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=8)
    date_condition = create_time >= (datetime.datetime.now()
                                     - datetime.timedelta(days=DAY))
    if (data['type'] == 'WatchEvent') and date_condition:
        if data['payload']['action'] == 'started':
            data['date_time'] = create_time.strftime("%Y-%m-%d %H:%M:%S")
            return True
    else:
        return False

def analyze(json_data):
    """
    分析获取的数据
    :return 符合过滤条件的数据
    """
    result_data = []
    for fi_data in json_data:
        if check_condition(fi_data):
            result_data.append(fi_data)
    return result_data
```

##### 3、生成发送邮件的内容：
最终邮件内容如下：
![](http://o6r0c5t2r.bkt.clouddn.com/github-bot-show.png)

**注意:** 因为获取项目stars数的接口，有的时候获取数据很慢，所以设置了超时时间。最好的方法因该是以异步的方式解决。可以参考[grequests项目](https://github.com/kennethreitz/grequests)
```python
CONTENT_FORMAT = """
    <table border="2" align="center">
      <tr>
        <th>头像</th>
        <th>用户名</th>
        <th>项目名</th>
        <th>starred日期</th>
        <th>项目star数量</th>
      </tr>
      {starred_info}
    </table>
"""

def make_content():
    """
    生成发布邮件的内容
    """
    json_data = get_data()
    data = analyze(json_data)
    content = []

    for fi_data in data:
        user = fi_data['actor']['login']
        user_url = 'https://github.com/' + user
        avatar_url = fi_data['actor']['avatar_url']
        repo_name = fi_data['repo']['name']
        repo_url = 'https://github.com/' + repo_name
        date_time = fi_data['date_time']
        try:
            repo_stars = requests.get(fi_data['repo']['url'], timeout=2).json()
            if repo_stars:
                repo_stars = repo_stars['stargazers_count']
            else:
                repo_stars = '未知数'
        except Exception as e:
            repo_stars = '未知数'
            logger.warning(u'获取：{} 项目星数失败——{}'.format(repo_name, e))
        starred_info = """<tr>
                            <td><img src={avatar_url} width=32px></img></td>
                            <td><a href={user_url}>{user}</a></td>
                            <td><a href={repo_url}>{repo_name}</a></td>
                            <td>{date_time}</td>
                            <td>{repo_stars}</td>
                          </tr>
                       """.format(user=user, repo_name=repo_name,
                                  repo_url=repo_url, user_url=user_url,
                                  avatar_url=avatar_url, repo_stars=repo_stars,
                                  date_time=date_time)
        content.append(starred_info)
    return content
```
##### 4、发送邮件：
如果是使用qq邮箱发送邮件，可以参考：[qq邮件服务文档](http://service.mail.qq.com/cgi-bin/help?id=28)

**注意:** 发送邮件使用的邮箱密码，最好用[授权码](http://service.mail.qq.com/cgi-bin/help?subtype=1&&no=1001256&&id=28)，因为我在测试邮件发送功能时，发送邮件的次数太多，后面突然不能发送了！而且没有任何错误提示，就卡在`sendmail`方法！后来登录qq邮箱，发现让我使用**授权码** 进行第三方授权。最后使用授权码一切就ok了！

发送邮件的函数如下：
```python
def send_email(receivers, email_content):
    """
    发送邮件
    """
    sender = MAIL['mail']  # 发送邮件的邮箱
    receivers = receivers   # 接收邮件的邮箱，可设置多个

    # 三个参数：第一个为文本内容，第二个 html 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(
        CONTENT_FORMAT.format(starred_info=''.join(email_content)),
        'html', 'utf-8'
    )
    message['From'] = Header(u'Github机器人', 'utf-8')
    message['To'] = Header(u'削微寒', 'utf-8')

    subject = u'今日Github热点'  # 设置邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtp_obj = smtplib.SMTP_SSL()  # qq邮箱要求是https连接，所以需要用SMTP_SSL
        smtp_obj.connect(MAIL['host'], MAIL['port'])    # 设置SMTP地址和端口号
        smtp_obj.login(MAIL['username'], MAIL['password'])
        smtp_obj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException as e:
        logger.error(u"无法发送邮件: {}".format(e))
```

**完整的代码**：[我的Github](https://github.com/521xueweihan/HelloGithub/tree/master/script)

## 最后
参照[ crontab 定时任务](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)，在linux下设置定时任务。
```
1. EDITOR=vi; export EDITOR #使用vi编辑器编辑

2. crontab -e #加入定时任务

3. crontab -l #查看是否加入成功
```

## TODO
1. 获取Explore页的数据

## 参考
- [requests文档](http://docs.python-requests.org/zh_CN/latest/index.html)
- [Linux工具快速教程](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)
- [wiki：时区](https://zh.wikipedia.org/wiki/%E6%97%B6%E5%8C%BA)
- [python时区问题](http://tech.glowing.com/cn/dealing-with-timezone-in-python/)
