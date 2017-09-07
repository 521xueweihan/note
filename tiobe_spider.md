## 爬虫



## 定时爬虫



1. 不挂代理无法显示 排名前十的语言图表
2. 使用xpath，由于 html 结构不规范，所以会有几个坑。参考：
	- http://python.jobbole.com/84689/
	- http://www.w3school.com.cn/xpath/xpath_syntax.asp
3. 正则，参考:
	- https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
	- 工具－http://tool.chinaz.com/regex
4. 图表 highcharts，参考:
	- https://www.hcharts.cn/demo/highcharts/line-basic

完成：
1. 解析整合前 50 语言的数据
2. 解析描述：title、description（需要翻译）
3. 解析图表数据，并显示

未完成：
1. 定时轮训 rss，以获取最新内容：https://www.tiobe.com/tiobe-index/rss.xml
2. 通知邮件（异常、获取到最新数据）
3. 编辑 描述（web app 提供编辑功能）


python date format

%a 星期缩写
%A 星期全拼
%b 月份缩写
%B 月份全拼
%c Date and time representation appropriate for locale
%d Day of month as decimal number (01 - 31)
%H Hour in 24-hour format (00 - 23)
%I Hour in 12-hour format (01 - 12)
%j Day of year as decimal number (001 - 366)
%m Month as decimal number (01 - 12)
%M Minute as decimal number (00 - 59)
%p Current locale's A.M./P.M. indicator for 12-hour clock
%S Second as decimal number (00 - 59)
%U Week of year as decimal number, with Sunday as first day of week (00 - 51)
%w Weekday as decimal number (0 - 6; Sunday is 0)
%W Week of year as decimal number, with Monday as first day of week (00 - 51)
%x Date representation for current locale
%X Time representation for current locale
%y Year without century, as decimal number (00 - 99)
%Y Year with century, as decimal number
%z, %Z Time-zone name or abbreviation; no characters if time zone is unknown
%% Percent sign
