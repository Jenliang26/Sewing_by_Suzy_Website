# Generated by Django 3.2.7 on 2021-09-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Statuses',
        ),
    ]
