# Generated by Django 2.0 on 2017-12-15 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ForwardingTable',
        ),
        migrations.DeleteModel(
            name='RoutingTable',
        ),
    ]