# Generated by Django 4.0.5 on 2022-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('itemname', models.CharField(max_length=100)),
            ],
        ),
    ]