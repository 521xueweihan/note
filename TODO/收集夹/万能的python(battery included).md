## json格式化工具
```
echo '{"foo": "lorem", "bar": "ipsum"}' | python -m json.tool
curl https://randomuser.me/api/ | python -m json.tool
```

## 本地启动server(可用于文件下载)
```
python -m SimpleHTTPServer 8000
```

## 使用默认浏览器打开url
```
python -m webbrowser
参数：
-n open new window
-t open new tab
url target url
```
