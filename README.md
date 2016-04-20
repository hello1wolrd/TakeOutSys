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
<ol>
<li><h5>python编码格式采用PEP8<h5></li>  
<li><h5>非关系数据使用mongodb进行存储<h5></li>  
<li><h5>缓存以及网站统计使用redis<h5></li>
<li><h5>队列使用celery+redis<h5></li> 
<li><h5>基本的用户信息采用MySql进行存储<h5></li>  
<li><h5>前端统一使用grant进行打包<h5></li>  
<li><h5>DJango采用Fat Models, Utility Modules, Thin Views, Stupid Templates 原则<h5></li>  
<li><h5>服务器采用centos + nginx + uwsgi 配置 , uwsgi管理系统使用The Master FIFO（详细配置见文档）<h5></li> 
<li><h5>Django、 python 等相关PyPi使用virtualwrapper进行管理  <h5></li>
</ol>

安装指令：
====
需求条件：
安装Python Package(具体查看requirement.txt)<br>
可以使用fabric一键安装pyp以及系统需求的软件包(我在centos上开发， 所以目前只有centos7版本)<br>
另外建议安装ipython<br>

安装MongoDB<br>
安装Redis<br>

启动redis<br>
启动mongodb<br>
启动celery <br>
启动django程序<br>

----------
后台还有很多需要完善
有事发504888883@qq.com
