# Generated by Django 3.1.4 on 2021-01-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentsManagement', '0011_auto_20210109_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='recipe_related',
        ),
    ]
