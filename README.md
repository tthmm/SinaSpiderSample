# 软件依赖
* js相关：nodejs 6.0，phantomJS
* python相关: python selenium

# 说明
c.py 爬取了新浪财经的网页，取出了第一页的数据
api.py 直接调用了该网页中获取数据的api，从而不需要载入网页就可以快速的获取数据
* * *
两个程序完全独立，分别输出与data.txt和api-data.txt