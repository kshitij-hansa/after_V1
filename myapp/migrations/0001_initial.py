# Generated by Django 3.2.9 on 2021-11-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
