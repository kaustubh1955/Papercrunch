# Generated by Django 2.2.1 on 2019-06-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0008_auto_20190620_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='google',
            field=models.BooleanField(default=False),
        ),
    ]
