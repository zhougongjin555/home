# Generated by Django 3.2.4 on 2021-08-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=16)),
                ('pwd', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
