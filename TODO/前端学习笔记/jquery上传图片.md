## 通过jQuery Ajax使用FormData对象上传文件

FormData对象，是可以使用一系列的键值对来模拟一个完整的表单，然后使用XMLHttpRequest发送这个"表单"。

在 Mozilla Developer 网站 使用FormData对象 有详尽的FormData对象使用说明。

但上传文件部分只有底层的XMLHttpRequest对象发送上传请求，那么怎么通过jQuery的Ajax上传呢？
本文将介绍通过jQuery使用FormData对象上传文件。

使用<form>表单初始化FormData对象方式上传文件
HTML代码
```html
<form id="uploadForm" enctype="multipart/form-data">
    <input id="file" type="file" name="file"/>
    <button id="upload" type="button">upload</button>
</form>
```

javascript代码  
```javascript
$.ajax({
    url: '/upload',
    type: 'POST',
    cache: false,
    data: new FormData($('#uploadForm')[0]),
    processData: false,
    contentType: false
}).done(function(res) {
}).fail(function(res) {});
```

这里要注意几点：
- processData设置为false。因为data值是FormData对象，不需要对数据做处理。
- form标签添加enctype="multipart/form-data"属性。
- cache设置为false，上传文件不需要缓存。
- contentType设置为false。因为是由<form>表单构造的FormData对象，且已经声明了属性enctype="multipart/form-data"，所以这里设置为false。
- 上传后，服务器端代码需要使用从查询参数名为file获取文件输入流对象，因为input中声明的是name="file"。

如果不是用form表单构造FormData对象又该怎么做呢？

使用FormData对象添加字段方式上传文件
HTML代码
```html
<div id="uploadForm">
    <input id="file" type="file"/>
    <button id="upload" type="button">upload</button>
</div>
```

这里没有form标签，也没有enctype="multipart/form-data"属性。

javascript代码
```javascript
var formData = new FormData();
formData.append('file', $('#file')[0].files[0]);
$.ajax({
    url: '/upload',
    type: 'POST',
    cache: false,
    data: formData,
    processData: false,
    contentType: false
}).done(function(res) {
}).fail(function(res) {});
```
这里有几处不一样：

append()的第二个参数应是文件对象，即$('#file')[0].files[0]。
contentType也要设置为‘false’。
从代码$('#file')[0].files[0]中可以看到一个input type="file"标签能够上传多个文件，
只需要在input type="file"里添加multiple或multiple="multiple"属性。

原文链接：http://www.jianshu.com/p/46e6e03a0d53
