# Generated by Django 4.2.1 on 2023-06-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(max_length=250)),
                ('freelance', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='pics')),
                ('image2', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
