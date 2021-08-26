# Generated by Django 3.2.4 on 2021-07-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapps', '0003_auto_20210704_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='foodapps.Product'),
        ),
    ]
