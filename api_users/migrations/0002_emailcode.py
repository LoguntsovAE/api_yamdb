# Generated by Django 3.0.5 on 2021-02-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('confirmation_code', models.CharField(max_length=9, verbose_name='Код подтвеждения')),
            ],
        ),
    ]
