# Generated by Django 4.0.5 on 2022-07-07 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdertoFoodList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.foodlist')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.order')),
            ],
        ),
    ]