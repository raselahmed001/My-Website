# Generated by Django 3.2.6 on 2021-08-18 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marchent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('no_of_restaurant', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('telephone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField()),
                ('mar_image', models.FileField(upload_to='images/mar_image/')),
                ('nid_driving_lic_image', models.ImageField(upload_to='images/nid/')),
                ('res_date', models.DateTimeField(auto_now_add=True)),
                ('validation_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socialmedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(blank=True, max_length=10, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_link', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='images/logo/')),
                ('banner', models.ImageField(upload_to='images/banner/')),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('telephone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField()),
                ('lit', models.CharField(max_length=200)),
                ('long', models.CharField(max_length=200)),
                ('trade_lic_image', models.FileField(upload_to='images/trade_lic/')),
                ('lic_validation_date', models.DateTimeField(blank=True, null=True)),
                ('res_validation_date', models.DateTimeField(blank=True, null=True)),
                ('mar_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.marchent')),
                ('social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food.socialmedia')),
            ],
        ),
        migrations.AddField(
            model_name='marchent',
            name='social',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food.socialmedia'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_image', models.ImageField(upload_to='images/user_cus/')),
                ('social', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food.socialmedia')),
            ],
        ),
    ]
