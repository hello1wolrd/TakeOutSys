# TakeOutSys
项目描述：
====
**********


技术点：
====
<ol>
后端
<li><h5>Python<h5></li>
<li><h5>DJango<h5></li>
<li><h5>django-unit-test<h5></li>
<li><h5>MongoDB<h5></li>
<li><h5>Mongoengine<h5></li>
<li><h5>Redis<h5></li>
<li><h5>Celery<h5></li>
<li><h5>SQL<h5></li>
<li><h5>fabric<h5></li>
<li><h5>logger<h5></li>

前端
<li><h5>AngularJs<h5></li>
<li><h5>Bootstrap<h5></li>
<li><h5>jQuery<h5></li>
<li><h5>HTML5<h5></li>
<li><h5>CSS3<h5></li>
</ol>


基本规范：
====
1、python编码格式采用PEP8  
2、非关系数据使用mongodb进行存储  
3、缓存以及网站统计使用redis
4、队列使用celery+redis 
5、基本的用户信息采用MySql进行存储  
6、前端统一使用grant进行打包  
7、DJango采用Fat Models, Utility Modules, Thin Views, Stupid Templates 原则  
8、服务器采用centos + nginx + uwsgi 配置 , uwsgi管理系统使用The Master FIFO（详细配置见文档） 
9、Django、 python 等相关PyPi使用virtualwrapper进行管理  


安装指令：
====
需求条件：
安装Python Package:
celery==3.1.23
Django==1.9.5
django-celery==3.1.17
mongoengine==0.10.6
MySQL-python==1.2.5
Pillow==3.2.0
pymongo==3.2.2
PyYAML==3.11
redis==2.10.5
可以使用fabric一键安装pypi以及系统需求的软件包（我在centos上开发， 所以目前只有centos7版本）
另外建议安装ipython

安装MongoDB
安装Redis

启动redis
启动mongodb
启动celery 
启动django程序

----------
后台还有很多需要完善
有事发504888883@qq.com
