# Generated by Django 3.2.3 on 2021-05-27 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('max_way', '0004_auto_20210527_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('min_image', models.ImageField(upload_to='imoges/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='min_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='max_way.minimage'),
        ),
    ]
