# Generated by Django 4.0.5 on 2022-07-08 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_ordertofoodlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='menu',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='warehouse.menu'),
            preserve_default=False,
        ),
    ]
