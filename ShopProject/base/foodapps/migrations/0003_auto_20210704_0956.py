# Generated by Django 3.2.4 on 2021-07-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapps', '0002_auto_20210704_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='foodapps.Category'),
        ),
    ]
