# Generated by Django 4.1.2 on 2022-12-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myLoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='ProdImg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
