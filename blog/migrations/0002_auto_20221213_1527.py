# Generated by Django 2.2.3 on 2022-12-13 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
