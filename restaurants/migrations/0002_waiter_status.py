# Generated by Django 3.1.7 on 2021-03-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waiter',
            name='status',
            field=models.CharField(choices=[('w', 'Wait'), ('r', 'Ready')], default='w', max_length=1),
        ),
    ]
