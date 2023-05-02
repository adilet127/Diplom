# Generated by Django 3.2.7 on 2023-04-27 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20230427_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='menu_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_rewiwes', to='myapp.menucategory'),
        ),
        migrations.AlterField(
            model_name='comingsoon',
            name='menu_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comsoon', to='myapp.menucategory'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='menu_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contactinfos', to='myapp.menucategory'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuitems', to='myapp.menucategory'),
        ),
        migrations.AlterField(
            model_name='restaurantinfo',
            name='menu_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants_infos', to='myapp.menucategory'),
        ),
    ]