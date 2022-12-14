# Generated by Django 4.1.2 on 2022-10-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelUsers',
            fields=[
                ('id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
