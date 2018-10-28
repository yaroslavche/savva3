# Generated by Django 2.1.2 on 2018-10-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_auto_20181028_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joke',
            old_name='publised',
            new_name='published',
        ),
        migrations.AlterField(
            model_name='joke',
            name='author',
            field=models.CharField(blank=True, max_length=100, verbose_name='Кто добавляет'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='text',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
