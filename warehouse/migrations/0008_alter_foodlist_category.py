# Generated by Django 4.0.5 on 2022-07-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0007_foodlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodlist',
            name='category',
            field=models.CharField(choices=[('Dimsum', 'Dimsum'), ('Chicken', 'Chicken'), ('Pastry', 'Pastry'), ('Sandwich', 'Sandwich'), ('Dessert', 'Dessert'), ('Drinks', 'Drinks')], default='Dimsum', max_length=100),
        ),
    ]