# Generated by Django 3.2.10 on 2022-01-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=300)),
            ],
            options={
                'verbose_name': 'Заявка пользователя',
                'verbose_name_plural': 'Заявки пользователей',
            },
        ),
    ]
