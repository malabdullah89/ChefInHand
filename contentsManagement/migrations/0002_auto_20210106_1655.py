# Generated by Django 3.1.4 on 2021-01-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentsManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='company_name',
        ),
        migrations.AddField(
            model_name='recipe',
            name='chef_name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='kitchen_type',
            field=models.ManyToManyField(default=None, to='contentsManagement.Kitchen'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.ManyToManyField(default=None, to='contentsManagement.MealType'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_info_arabic',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_info_english',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='recipe',
            name='section',
            field=models.ManyToManyField(default=None, to='contentsManagement.Section'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_time',
            field=models.CharField(default=None, max_length=100),
        ),
    ]