# Generated by Django 3.2.7 on 2021-09-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]