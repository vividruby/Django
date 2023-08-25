# Generated by Django 4.2.4 on 2023-08-25 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_alter_restaurant_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='date',
        ),
    ]
