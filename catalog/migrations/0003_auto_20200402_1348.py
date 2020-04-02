# Generated by Django 3.0.2 on 2020-04-02 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200127_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='is_readed',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Is it active?'),
        ),
        migrations.AlterField(
            model_name='language',
            name='idiom',
            field=models.CharField(help_text='enter the language', max_length=20),
        ),
    ]
