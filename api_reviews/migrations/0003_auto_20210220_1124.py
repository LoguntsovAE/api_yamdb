# Generated by Django 3.0.5 on 2021-02-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_reviews', '0002_auto_20210220_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
