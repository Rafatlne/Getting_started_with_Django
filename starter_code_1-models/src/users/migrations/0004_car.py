# Generated by Django 3.1.7 on 2021-02-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_website_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
    ]
