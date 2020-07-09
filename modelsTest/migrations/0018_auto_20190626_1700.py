# Generated by Django 2.2.1 on 2019-06-26 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0017_learner_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learner',
            name='avatarId',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(0)]),
        ),
    ]
