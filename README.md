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


项目（Project） Vs 应用（Apps）

	项目与应用之间有什么不同之处？应用是一个提供功能的 Web 应用 – 例如：一个博客系统、 一个公共记录的数据库或者一个简单的投票系统。项目是针对一个特定的 Web 网站相关的配置和其应用的组合。一个项目可以包含多个应用。 一个应用可以在多个项目中使用。

在Django中编写一个有数据库支持的Web应用的第一步就是定义模型，从本质上讲就是数据库设计及其附加的元数据。

	模型是有关你数据的唯一且明确的数据源。 它包含了你所要存储的数据的基本字段和行为。 Django 遵循 DRY 原则 。 目标是为了只在一个地方定义你的数据模型就可从中自动获取数据。


那么接下来就是为该应用创建对应的数据库架构（create table statements），为Poll和Choice 对象创建Python访问数据库的API。当然在此之前我们需要再次编辑settings.py文件，在INSTALLED_APPS设置中加入'polls'字符，告诉我们的项目已经安装了polls应用。

	Django 应用是“可插拔的”：你可以在多个项目使用一个应用， 你还可以分发应用， 因为它们没有被捆绑到一个给定的 Django 安装环境中。

运行python manage.py sql polls 生成相关的create table sql语句：

	BEGIN;
	CREATE TABLE "polls_poll" (
	    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	    "question" varchar(200) NOT NULL,
	    "pub_date" datetime NOT NULL
	)
	;
	CREATE TABLE "polls_choice" (
	    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	    "poll_id" integer NOT NULL REFERENCES "polls_poll" ("id"),
	    "choice_text" varchar(200) NOT NULL,
	    "votes" integer NOT NULL
	)
	;
	COMMIT;

注意此时，SQL 语句并没有运行，如果你愿意可以直接复制这个语句在数据库命令行中运行，但是Django提供了更简单的方法来执行此SQL。

运行python manage.py syncdb在数据库中创建模型对应的表。syncdb 命令会给在 INSTALLED_APPS 中有但数据库中没有对应表的应用执行 sqlall 操作。


	$ python manage.py syncdb 
	/usr/local/lib/python2.7/dist-packages/Django-1.8.16-py2.7.egg/django/core/management/commands/syncdb.py:24: RemovedInDjango19Warning: The syncdb command will be removed in Django 1.9
	  warnings.warn("The syncdb command will be removed in Django 1.9", RemovedInDjango19Warning)

	Operations to perform:
	  Synchronize unmigrated apps: staticfiles, polls, messages
	  Apply all migrations: admin, contenttypes, auth, sessions
	Synchronizing apps without migrations:
	  Creating tables...
	    Creating table polls_poll
	    Creating table polls_choice
	    Running deferred SQL...
	  Installing custom SQL...
	Running migrations:
	  No migrations to apply.




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


