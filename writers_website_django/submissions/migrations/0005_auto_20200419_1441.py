# Generated by Django 3.0.5 on 2020-04-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_auto_20200419_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Themes',
        ),
        migrations.AddField(
            model_name='submission',
            name='themes',
            field=models.ManyToManyField(blank=True, to='submissions.Theme'),
        ),
    ]
