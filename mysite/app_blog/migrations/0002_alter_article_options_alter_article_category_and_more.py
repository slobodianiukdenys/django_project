# Generated by Django 5.2 on 2025-04-23 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Статя', 'verbose_name_plural': 'Статті'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='app_blog.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_page',
            field=models.BooleanField(default=True, help_text='Показувати на головній сторінці', verbose_name='Головна'),
        ),
    ]
