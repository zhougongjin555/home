from django.db import models

# Create your models here.


class Employee(models.Model):
    # AutoField，自增
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    gender = models.BooleanField()
    birthday = models.DateField()
    department = models.CharField(max_length=32)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name  # 默认显示这个变量，但是返回的仍然是包含全部变量的整个对象

