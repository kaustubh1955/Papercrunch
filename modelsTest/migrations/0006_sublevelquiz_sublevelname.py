# Generated by Django 2.2.1 on 2019-06-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0005_auto_20190618_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='sublevelquiz',
            name='subLevelName',
            field=models.CharField(default='Test Quiz', max_length=300),
            preserve_default=False,
        ),
    ]
