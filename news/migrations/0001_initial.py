# Generated by Django 5.0.2 on 2024-02-13 07:00

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='دسته بندی')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name='لینک دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='تگ')),
                ('url', models.CharField(blank=True, max_length=250, null=True, verbose_name='لینک تگ')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True, verbose_name='عنوان خبر')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='متن خبر')),
                ('author', models.CharField(max_length=250, null=True, verbose_name='نویسنده خبر')),
                ('created_date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('selected', models.BooleanField(default=False, verbose_name='خبر برگزیده')),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.ManyToManyField(to='news.category', verbose_name='دسته بندی')),
                ('tag', models.ManyToManyField(to='news.tag', verbose_name='تگ خبر')),
            ],
        ),
    ]
