# Generated by Django 3.1.2 on 2020-10-24 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentType',
            field=models.BooleanField(default=True),
        ),
    ]
