# Generated by Django 3.1.2 on 2020-10-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201024_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(choices=[('P', 'positive'), ('N', 'negitive')], default='P', max_length=2),
        ),
    ]
