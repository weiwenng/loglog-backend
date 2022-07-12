# Generated by Django 4.0.5 on 2022-07-12 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_logistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logistics',
            old_name='logslimit',
            new_name='base_limit',
        ),
        migrations.RenameField(
            model_name='logistics',
            old_name='logscategory',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='logistics',
            old_name='logsdescription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='logistics',
            old_name='logsname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='logistics',
            old_name='logsprice',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='logistics',
            old_name='logsquantity',
            new_name='quantity',
        ),
    ]
