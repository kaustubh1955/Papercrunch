# Generated by Django 2.2.1 on 2019-06-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0009_learner_google'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='currentProgress',
            field=models.CharField(default='[0, 0, 0]', max_length=300),
        ),
        migrations.AlterField(
            model_name='learner',
            name='badges',
            field=models.CharField(default='[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', max_length=300),
        ),
    ]
