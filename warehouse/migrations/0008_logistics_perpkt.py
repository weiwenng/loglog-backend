# Generated by Django 4.0.5 on 2022-07-12 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_rename_logslimit_logistics_base_limit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logistics',
            name='perpkt',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
