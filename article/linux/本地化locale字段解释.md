## locale相关（环境）变量生效的优先顺序：
1. LANGUAGE 指定个人对语言环境值的主次偏好，例如zh_CN:en_US:en
2. LC_ALL 这不是一个环境变量，是一个可被C语言库函数setlocale设置的宏，其值可覆盖所有其他的locale设定。因此缺省时此值为空
3. LC_xxx 可设定locale各方面（category）的值，可以覆盖LANG的值。
4. LANG 指定默认使用的locale值


## locale字段解释
1、语言符号及其分类(LC_CTYPE)
2、数字(LC_NUMERIC)
3、比较和排序习惯(LC_COLLATE)
4、时间显示格式(LC_TIME)
5、货币单位(LC_MONETARY)
6、信息主要是提示信息,错误信息,状态信息,标题,标签,按钮和菜单等(LC_MESSAGES)
7、姓名书写方式(LC_NAME)
8、地址书写方式(LC_ADDRESS)
9、电话号码书写方式(LC_TELEPHONE)
10、度量衡表达方式 (LC_MEASUREMENT)
11、默认纸张尺寸大小(LC_PAPER)
12、对locale自身包含信息的概述(LC_IDENTIFICATION)。
