# Generated by Django 3.1.2 on 2020-12-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='text', max_length=250),
            preserve_default=False,
        ),
    ]