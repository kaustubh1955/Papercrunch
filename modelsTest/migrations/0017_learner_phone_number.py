# Generated by Django 2.2.1 on 2019-06-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0016_learner_avatarid'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='phone_number',
            field=models.CharField(default='+00000000000000', max_length=15),
        ),
    ]
