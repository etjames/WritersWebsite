# Generated by Django 3.0.5 on 2020-04-20 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0008_auto_20200420_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='genres',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='themes',
            new_name='theme',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='writing_types',
            new_name='writing_type',
        ),
    ]
