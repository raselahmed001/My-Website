# Generated by Django 3.2.4 on 2021-08-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]