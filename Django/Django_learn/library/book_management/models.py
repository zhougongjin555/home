from django.db import models

# Create your models here.

# book--publiush 一对多
# author--authordetail  一对一
# book--author 多对多


# 作者详情表
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)
    def __str__(self):
        return self.name

'''
    # 与AuthorDetail建立一对一的关系
    authorDetail = models.OneToOneField(
        to="AuthorDetail", on_delete=models.CASCADE)
'''
'''
# 作者基本信息表
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)
    def __str__(self):
        return self.addr
'''

# 出版社信息
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32, null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return str(self.nid)



# 书籍信息
class Book(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方，自动在后面拼"_id"
    publish = models.ForeignKey(
        to="Publish",
        to_field="nid",
        on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField(to='Author',)

    def __str__(self):
        return self.title

