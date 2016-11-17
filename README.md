===Django 源码阅读笔记


> README Of django-ccsds


	Version: django 1.8.16 
	Date: 2016.11.16
	Author: Wayne

最近在参与一个项目－CCSDS，因项目需要，故打算学习django框架，而本仓库的建立是为了跟踪我的django学习历程。如此优秀的框架，如此优秀的代码，当然得拿来好好的研究一番，那么就从阅读源码开始。当然学习django起于源码而不仅仅停留于源码，还会做一些系统的总结，因此学习的大概形式是采用源码＋注释＋总结。

 #### Django 源码学习１：建立Project和App　django: django-admin.py startproject mysite /  project: mange.py startapp polls

 #### Django 源码学习２：一个纯粹有Python编写的轻量Ｗeb服务器　runserver.py

