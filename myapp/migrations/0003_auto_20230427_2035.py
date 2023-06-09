# Generated by Django 3.2.7 on 2023-04-27 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230427_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantinfo',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О на'},
        ),
        migrations.AlterField(
            model_name='clientreview',
            name='star_nbr',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='restaurantinfo',
            name='menu_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants_infos', to='myapp.menucategory'),
        ),
    ]
