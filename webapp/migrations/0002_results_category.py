# Generated by Django 3.0.3 on 2020-02-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='CATEGORY',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
