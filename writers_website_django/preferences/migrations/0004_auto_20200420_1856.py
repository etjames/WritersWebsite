# Generated by Django 3.0.5 on 2020-04-20 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0003_auto_20200420_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='user',
            new_name='puser',
        ),
    ]
