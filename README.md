===Django 源码阅读笔记


> README Of django-ccsds


	Version: django 1.8.16 
	Date: 2016.11.16
	Author: Wayne

最近在参与一个项目－CCSDS，因项目需要，故打算学习django框架，而本仓库的建立是为了跟踪我的django学习历程。如此优秀的框架，如此优秀的代码，当然得拿来好好的研究一番，那么就从阅读源码开始。当然学习django起于源码而不仅仅停留于源码，还会做一些系统的总结，因此学习的大概形式是采用源码＋注释＋总结。


 
#### Django 源码学习１：建立Project和App

 django: django-admin.py startproject mysite /  project: mange.py startapp polls

#### Django 源码学习２：一个纯粹由Python编写的轻量Ｗeb服务器

 runserver.py


#### Django 源码学习3：基于正则表达式的URL分派


#### Django 源码学习4：中间件(Middleware)支持

允许对请求处理的各个阶段进行干涉

#### Django 源码学习5：视图（Views）模块

Views模块并不是Django中必须的，但它的存在简化了Django的开发

#### Django 源码学习6：db.models 模块

Django 的db模块包含models和backends，models中定义了与数据库对应的各种fields和生成sql的rules，backends里则包含了对mysql、oracle、postgresql、sqlite3的支持。

#### Django 源码学习7 ：admin.auth模块

admin.auth是django的权限模块。

#### Django 源码学习8：Session 存储

#### Django 源码学习9：Password 的生成和验证

#### Django 源码学习10：Template(模板)

#### Django 源码学习11： Form(表单)类

#### Django 源码学习12：Django安全机制


