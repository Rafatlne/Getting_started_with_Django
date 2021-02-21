# Generated by Django 3.1.7 on 2021-02-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(to='users.Car', verbose_name="the user's cars"),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name="person's first name"),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name="person's last name"),
        ),
    ]