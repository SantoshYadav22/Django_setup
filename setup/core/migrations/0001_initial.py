# Generated by Django 3.2.8 on 2021-10-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studid', models.IntegerField()),
                ('studname', models.CharField(max_length=100)),
                ('studmail', models.EmailField(max_length=70)),
                ('studpass', models.CharField(max_length=100)),
            ],
        ),
    ]
