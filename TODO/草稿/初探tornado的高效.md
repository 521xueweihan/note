## Tornado
tornado的框架通过非阻塞、异步的方式来处理‘高并发’的问题。

主要是通过操作系统的库：ee


### IOLoop对象
这个是实现非阻塞的核心，文档中对IOLoop对象的解释是：
> An I/O event loop for non-blocking sockets.

首先IOLoop对象其实就是一个：非阻塞socket，中间那段'I/O event loop'，意思是：通过I/O事件循
环机制，实现非阻塞。

socket就是一个I/O操作，会造成阻塞。为提高效率、并发量，不能因为建立一个socket链接就花去大量事
件，所以先不管三七二十一，只要有建立链接的请求一律接收，然后丢给epoll，当链接建立好了，有数据传
过来了epoll就会发送消息
