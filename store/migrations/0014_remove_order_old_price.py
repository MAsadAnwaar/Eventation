# Generated by Django 3.2.7 on 2021-09-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_order_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='old_price',
        ),
    ]
