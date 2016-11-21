===Django 源码阅读笔记


> README Of django-ccsds


	Version: django 1.8.16 
	Date: 2016.11.16
	Author: Wayne


最近在参与一个项目－CCSDS，因项目需要，故打算学习django框架，而本仓库的建立是为了跟踪我的django学习历程。如此优秀的框架，如此优秀的代码，当然得拿来好好的研究一番，那么就从阅读源码开始。当然学习django起于源码而不仅仅停留于源码，还会做一些系统的总结，因此学习的大概形式是采用源码＋注释＋总结。

	如有什么不妥的地方，欢迎批评指正，同时也非常欢迎您加入进来，一起阅读源码，一起讨论，一起进步！--- Wayne 2016.11.17


 
#### Django 源码学习01：建立Project和App

 	django: django-admin.py startproject mysite
 	project: mange.py startapp polls1


** 项目（Project） Vs 应用（Apps）**

	项目与应用之间有什么不同之处？应用是一个提供功能的 Web 应用 – 例如：一个博客系统、 一个公共记录的数据库或者一个简单的投票系统。项目是针对一个特定的 Web 网站相关的配置和其应用的组合。一个项目可以包含多个应用。 一个应用可以在多个项目中使用。

在Django中编写一个有数据库支持的Web应用的第一步就是定义模型，从本质上讲就是数据库设计及其附加的元数据。

	模型是有关你数据的唯一且明确的数据源。 它包含了你所要存储的数据的基本字段和行为。 Django 遵循 DRY 原则 。 目标是为了只在一个地方定义你的数据模型就可从中自动获取数据。

#### Django 源码学习02：一个纯粹由Python编写的轻量Ｗeb服务器

 	runserver.py

#### Django 源码学习03：基于正则表达式的URL分派


#### Django 源码学习04：中间件(Middleware)支持

	允许对请求处理的各个阶段进行干涉

#### Django 源码学习05：视图（Views）模块

	Views模块并不是Django中必须的，但它的存在简化了Django的开发

#### Django 源码学习06：db.models 模块

	Django 的db模块包含models和backends；
	models中定义了与数据库对应的各种fields和生成sql的rules；
	backends里则包含了对mysql、oracle、postgresql、sqlite3的支持。

#### Django 源码学习07：admin.auth模块

	admin.auth是django的权限模块。

#### Django 源码学习08：Session 存储

#### Django 源码学习09：Password 的生成和验证

#### Django 源码学习10：Template(模板)

#### Django 源码学习11：Form(表单)类

#### Django 源码学习12：Django安全机制


