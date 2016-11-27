# coding:utf-8

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

"""
当有人访问你的网站页面，如"/polls/34/"时，Django会加载mysite.urls模块，这是因为ROOT_URLCONF设置指向它。
接着在该模块中寻找名为urlpatterns的变量并以此匹配其中的正则表达式。
include()可以让我们便利的引用的其他的URLconfs。
请注意include()中正则表达式没有$结尾匹配符，而是一个反斜杠。
当Django解析include()时，它截取的URL那部分而把剩余的字符串交由加载进来的URLconf作进一步处理。
include()背后隐藏的想法是使URLs即插即用。
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),

]
