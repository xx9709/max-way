# Generated by Django 3.2.3 on 2021-05-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max_way', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pay_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
