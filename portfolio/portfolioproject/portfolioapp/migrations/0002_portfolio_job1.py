# Generated by Django 4.2.1 on 2023-06-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='job1',
            field=models.TextField(default='wedeveloper'),
            preserve_default=False,
        ),
    ]
