# Generated by Django 3.1.4 on 2021-01-09 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('contentsManagement', '0005_auto_20210106_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='chef_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.chef'),
        ),
    ]
