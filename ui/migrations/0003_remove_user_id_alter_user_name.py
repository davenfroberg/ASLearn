# Generated by Django 4.2.7 on 2023-11-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]