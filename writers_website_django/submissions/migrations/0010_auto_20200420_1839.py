# Generated by Django 3.0.5 on 2020-04-20 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0009_auto_20200420_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='author_name',
            field=models.CharField(help_text='You can write Anonymous, or a name/pseudonym if wanted', max_length=128),
        ),
        migrations.AlterField(
            model_name='submission',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.Genre'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.Theme'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='writing_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.WritingType'),
        ),
    ]
