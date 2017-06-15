## Flask 日志设置

```python
import logging
from logging.handlers import RotatingFileHandler
import traceback

from flask import Flask, request


app = Flask(__name__)


@app.after_request
def after_request(response):
    logger.info('%s %s %s %s %s', request.method,
                request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
                request.scheme, request.full_path, response.status)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    logger.error('%s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                 request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
                 request.method, request.scheme, request.full_path, tb)
    return '500 INTERNAL SERVER ERROR', 500

handler = RotatingFileHandler('%s.log' % app.name, maxBytes=1000000, backupCount=3)
logger = logging.getLogger(app.name)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


# 后面记录 log 统一用 logger 就 OK 了
```


参考：
- [stackoverflow-flask log](https://stackoverflow.com/questions/14037975/how-do-i-write-flasks-excellent-debug-log-message-to-a-file-in-production)
