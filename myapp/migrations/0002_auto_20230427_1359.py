# Generated by Django 3.2.7 on 2023-04-27 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comingsoon',
            options={'verbose_name': 'Скоро выйдет', 'verbose_name_plural': 'Скоро выйдет'},
        ),
        migrations.AlterModelOptions(
            name='menucategory',
            options={'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Блюда', 'verbose_name_plural': 'Блюды'},
        ),
        migrations.AlterModelOptions(
            name='restaurantinfo',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
    ]