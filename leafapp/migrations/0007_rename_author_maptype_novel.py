# Generated by Django 3.2.10 on 2021-12-29 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leafapp', '0006_alter_maptype_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maptype',
            old_name='author',
            new_name='novel',
        ),
    ]
