# Generated by Django 3.0.2 on 2020-04-02 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200402_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.ManyToManyField(blank=True, to='catalog.Book_readed'),
        ),
    ]
