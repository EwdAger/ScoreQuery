# 湖科大教务系统成绩查询

这个重中之重的项目终于开始立项啦~快开学了，要开始做点正事了。撒花撒花

## TODO LIST

### 爬虫部分

- 模拟登陆至教务网
- 通过Request URL访问成绩信息
- 将成绩信息录入数据库

### 查询网站构建

- 目前采用SQLite数据库（因为数据量略大，后期估计得换MySQL）
- 前端提供查询功能
- 微信接口

### 有关细节补充
- 班主任登录入口

暂定先不设置班主任注册接口，每一年都有新的老师成为班主任，还有有的老师是几个班的班主任（？）
，数据表里有关班主任的结构有待商榷。

- 毕业学生数据批量删除

实现部分倒是很简单，但是有的学生大四没修满学分还不能毕业。。所以这部分学生成绩应该还得留着。

- 数据更新问题

涉及到教务网服务器的问题，因为考完试后，估计班主任每天都会闲着没事查一下，
但是每查一次就下载一个总表有点太伤害教务网的土豆服务器了，所以到底是每隔多少天更新一次数据表
还是提供一个更新数据的按钮比较好。

## 更新日志
**V0.2.0更新**

- 终于使用selenium方法成功模拟登录
- 删除废弃代码

**V0.1.5更新**

- 确认了登录失败原因是post中缺少x, y两个动态校验值，但是尚不明确x, y值是如何产生的。。
- 尝试使用selenium方法进行模拟登陆

**V0.1.4更新**

- 其实并没有登录进教务网，网页又重定向到登录界面了
- 感觉应该可能是post的信息不对（诡异的x, y数据）
- 啊。。爬虫部分感觉要停滞了啊。。

**V0.1.3更新**

- 成功模拟登陆至教务网（大概？反正返回了200）
- 明天再做成绩部分的爬虫~


**V0.1.2更新**

- 使用Scrapy框架进行数据爬取，放弃愚蠢的单线程造轮子。。。。
- 巫师3真好玩


**V0.1.1更新**

- 更新爬虫部分代码，已有大致的框架

**V0.1 更新**

- 正式立项，确立开发计划 