# Generated by Django 2.2.1 on 2019-06-28 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0018_auto_20190626_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sublevelconcepts',
            name='conceptText',
        ),
        migrations.AddField(
            model_name='sublevelconcepts',
            name='conceptTextOne',
            field=models.TextField(default='Text', null=True),
        ),
        migrations.AddField(
            model_name='sublevelconcepts',
            name='conceptTextThree',
            field=models.TextField(default='Text', null=True),
        ),
        migrations.AddField(
            model_name='sublevelconcepts',
            name='conceptTextTwo',
            field=models.TextField(default='Text', null=True),
        ),
    ]
