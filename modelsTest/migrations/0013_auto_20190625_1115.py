# Generated by Django 2.2.1 on 2019-06-25 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelsTest', '0012_auto_20190624_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learner',
            name='currentProgress',
        ),
        migrations.CreateModel(
            name='LevelProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelOne', models.BooleanField(default=False)),
                ('levelTwo', models.BooleanField(default=False)),
                ('levelThree', models.BooleanField(default=False)),
                ('levelFour', models.BooleanField(default=False)),
                ('levelFive', models.BooleanField(default=False)),
                ('levelSix', models.BooleanField(default=False)),
                ('levelSeven', models.BooleanField(default=False)),
                ('levelEight', models.BooleanField(default=False)),
                ('levelNine', models.BooleanField(default=False)),
                ('learner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currentProgress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
