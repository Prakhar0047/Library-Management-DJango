# Generated by Django 3.0.4 on 2020-06-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200616_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.IntegerField(choices=[(0, 'Issued'), (1, 'Nt Issued')], default=0),
        ),
    ]