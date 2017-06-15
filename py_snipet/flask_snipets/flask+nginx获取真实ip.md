
## Nginx 配置
```
location / {
	proxy_set_header   Host             $host;
	proxy_set_header   X-Real-IP        $remote_addr;
	proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;

	proxy_redirect     off;
	proxy_pass         http://0.0.0.0:4333;


}
```

## Flask 获取真实 IP 代码片段
```python
request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
```
