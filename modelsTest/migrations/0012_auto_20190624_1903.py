# Generated by Django 2.2.1 on 2019-06-24 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0011_auto_20190624_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badges',
            old_name='Learner',
            new_name='learner',
        ),
    ]
