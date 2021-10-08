运行帮助：
1， cmd创建books_management数据库，一字不差（create database blog_object charset=UTF8;）

2， 终端进入项目根目录，执行python manage.py makemigrations
3， 执行python manage.py migrate创建django数据表

////或者直接运行我的data.sql导入到你的数据库，里面是我测试时候用到的部分数据，库名一定要是blog_object


直接进入主网站('/main')即可，有用的接口有文章标题、姓名、登陆注册（验证码有点反人类，看不出来去终端看）

进入文章最下面有点赞和评论、评论树（点击才显示）功能，事件原因，没有设计美化，能跑就行，=V=

然后通过个人主页的管理按钮进入后台，进行添加文章操作，编辑删除功能没时间弄了，但是可以通过ajax结合ORM实现，很简单


基本就这些了，功能不多。




富文本编辑器的上传图片功能有bug，界面一直转圈显示上传中，但是实际已经上传成功了，尝试解决，未果