## 步骤
1. 去官网下载：https://highlightjs.org/
2. 在页面上引入，样式css和highlight.js静态文件
3. 加入一段js代码，使得highlight.js生效，分析`<pre><code></code></pre>`标签中的内容，实现代码高亮：
```javascript
<script>hljs.initHighlightingOnLoad();</script>
```

## 实例：
**注意**：我的css和js都放到了`static`目录下
```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <!-- Hightlight.css -->
        <!-- 我选用的是hybrid主题 -->
        <link href="/static/css/hybrid.css" rel="stylesheet">
    </head>

    <body>
		<pre><code class="language-py">
			def open(self, doc_uuid=None):
			   if doc_uuid is None:
			       self.uuid = str(uuid.uuid4())
		</code></pre>
    <!-- hightlight.js -->
    <script src="/static/js/highlight.pack.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>
```

## 坑
现在有一个问题:因为文章中有代码块，代码块中的代码片段可以通过highlight.js转变成
安全的内容。但是如果对用户输入的全部内容进行转义，则会造成：代码块中的代码显示出错。

解决办法：使用正则匹配，对非`<pre></pre>`标签内容进行转义。  
终极解决办法：这个问题把我都弄崩溃了，其实问题很简单，因为highlight.js对于'lt'和'gt'会渲染
成高亮，导致转移后的'>'和'<'，html无法识别！所以只需要，反转义代码块中的`&amp;`。我靠坑啊！
```python
def code_unescape(s):
    """
    代码块中的内容不转义
    """
    s = s.group(0)
    # 反转义"&amp;"，使得'<','>'是html转义的符号。
    # hightligth.js有个坑，lg和lt会高亮，使得html识别不了"&lt;"和"&gt;"。
    s = s.replace("&amp;", "&")
    return s

content = unicode(markdown2.markdown(escape.html_escape(content),
                                     extras=['fenced-code-blocks']))
# 反转义代码块中的"&amp;"
m = re.compile('\<pre\>[\s\S]*\<\/pre\>')
content = m.sub(code_unescape, content)

```

参考：
- [ghostchina](http://www.ghostchina.com/adding-syntax-highlighting-to-ghost-using-highlight-js/)
- [highlight](https://github.com/trentm/python-markdown2/wiki/fenced-code-blocks)
- [markdown以及highlight](http://www.cnblogs.com/smdm/p/5323140.html)
