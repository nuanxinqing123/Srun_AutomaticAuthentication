# 项目说明
“深澜” 认证系统有很多不同的版本在被实际使用，有客户端版也有网页认证版，现在仅讨论网页版（Web 版）认证系统的自动登陆实现。

## 项目思路
来源于[ytf4425/Srun_login](https://github.com/ytf4425/Srun_login/)

## 项目介绍

项目环境：selenium、flask

srun_login.py：大家可以根据自己的学校自行修改29行处的地址，因为我们学校是内网认证，所以我直接写了内网地址，使用的话更改自己的学校认证地址即可，再33-34行修改需要认证的账号

chromedriver.exe：项目里面这个谷歌浏览器驱动是：91.0.4472.101,如果你和我的版本一致那就直接使用即可。其他版本的用户下载后，解压覆盖目录里的版本即可

查看自己的浏览器版本：[关于Chrome](https://jingyan.baidu.com/article/f0e83a25e1e06962e59101f3.html)

驱动下载地址：[淘宝镜像站](http://npm.taobao.org/mirrors/chromedriver/)

## 全自动认证思路
其实我目前的自动认证思路还是很菜，我用的方法是使用Flask框架绑定一个路由的GET请求去调用认证函数，详细可以查看app.py。然后我设置了定时任务，每隔三分钟自动访问一次绑定函数的路由，做到全自动认证，但是这个项目的玩法不止这样，其他的玩法暂时不适合公布，大家就自行开发吧。