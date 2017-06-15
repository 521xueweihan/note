> 本文参考整理于：https://imququ.com/post/four-ways-to-post-data-in-http.html

## 简介
这里介绍了，用 POST 方法提交数据时，常见的三种方式：
- application/x-www-form-urlencoded
- multipart/form-data
- application/json


## application/x-www-form-urlencoded（默认）
`<form>` 默认是以 `application/x-www-form-urlencoded` 方式提交数据，请求示例如下：
```
POST http://www.example.com HTTP/1.1
Content-Type: application/x-www-form-urlencoded;charset=utf-8

title=test&sub%5B%5D=1&sub%5B%5D=2&sub%5B%5D=3
```

## multipart/form-data（上传文件）
使用表单 **上传文件** 时，必须指明 `<form>` 表单的 `enctype` 的值为 `multipart/form-data`。

这种方式，首先生成了一个 boundary 用于分割不同的字段，然后 `Content-Type` 里指明了数据是以 `multipart/form-data` 来编码。最后，消息主体里按照字段个数又分为多个结构类似的部分，每部分都是以 `--boundary` 开始，紧接着是内容描述信息，然后是回车，最后是字段具体内容（文本或二进制），请求示例如下：
```
POST http://www.example.com HTTP/1.1
Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryrGKCBY7qhFd3TrwA

------WebKitFormBoundaryrGKCBY7qhFd3TrwA
Content-Disposition: form-data; name="text"

title
------WebKitFormBoundaryrGKCBY7qhFd3TrwA
Content-Disposition: form-data; name="file"; filename="chrome.png"
Content-Type: image/png

PNG ... content of chrome.png ...
------WebKitFormBoundaryrGKCBY7qhFd3TrwA--
```

## application/json（JSON）
这种方案，可以方便的提交复杂的结构化数据，特别适合 `RESTful` 的接口，此类接口可以通用在客户端和网页端。

把响应头的 `Content-Type` 设置为 `application/json`，用来告诉服务端消息主体是序列化后的 `JSON` 字符串，请求示例如下：
```
POST http://www.example.com HTTP/1.1
Content-Type: application/json;charset=utf-8

{"title":"test","sub":[1,2,3]}
```

## 参考
- [四种常见的 POST 提交数据方式](https://imququ.com/post/four-ways-to-post-data-in-http.html)
