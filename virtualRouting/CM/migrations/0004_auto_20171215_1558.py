# Generated by Django 2.0 on 2017-12-15 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CM', '0003_routingtable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='routingtable',
            old_name='networkDest',
            new_name='network_dest',
        ),
        migrations.RenameField(
            model_name='routingtable',
            old_name='nextHop',
            new_name='next_hop',
        ),
    ]
