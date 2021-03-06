# Generated by Django 3.2.4 on 2021-08-09 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('salary', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('experience', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('dateofbirth', models.DateField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Other', 'Other'), ('Male', 'Male')], max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('company', models.ManyToManyField(blank=True, to='jobportal.Company')),
            ],
        ),
    ]
