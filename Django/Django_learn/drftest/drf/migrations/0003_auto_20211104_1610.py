# Generated by Django 3.2.4 on 2021-11-04 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_userinfo_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='role',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(default='', max_length=64, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='level',
            field=models.IntegerField(choices=[(1, '普通会员'), (2, 'VIP'), (3, 'SVIP')], default=1, verbose_name='级别'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='drf.department', verbose_name='部门'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(to='drf.Role', verbose_name='角色'),
        ),
    ]
