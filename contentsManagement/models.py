from django.db import models
from accounts.models import User


class Section(models.Model):
    section_english_name = models.CharField(max_length=200)
    section_arabic_name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.section_english_name


class Type(models.Model):
    type_english_name = models.CharField(max_length=200)
    type_arabic_name = models.CharField(max_length=200)
    type_hindi_name = models.CharField(max_length=200, default=None)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)

    def __str__(self):
        return self.type_english_name


class Kitchen(models.Model):
    english_name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)

    def __str__(self):
        return self.english_name


class MealType(models.Model):
    english_name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)

    def __str__(self):
        return self.english_name


class Unit(models.Model):
    unit_english_name = models.CharField(max_length=200)
    unit_arabic_name = models.CharField(max_length=200)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=None)
    created_date = models.DateTimeField(default=None)

    def __str__(self):
        return self.unit_english_name


class Ingredient(models.Model):
    proudect_english_name = models.CharField(max_length=200)
    proudect_arabic_name = models.CharField(max_length=200)
    barcode_number = models.CharField(max_length=200)
    proudect_company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.proudect_english_name


class Sauce(models.Model):
    sauce_english_name = models.CharField(max_length=100)
    sauce_arabic_name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.sauce_english_name


class Step(models.Model):
    order_number = models.IntegerField()
    step_on_english = models.CharField(max_length=200)
    step_on_arabic = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_on_english


class Recipe(models.Model):
    PRICE_CHOICES = (
        ('Free', 'Free'),
        ('$1', '$1'),
        ('$2', '$2'),
        ('$3', '$3'),
        ('$4', '$4'),
        ('$5', '$5')

    )
    chef_name = models.ForeignKey('accounts.Chef', on_delete=models.CASCADE, null=True, default=None)
    kitchen_type = models.ForeignKey('Kitchen', on_delete=models.CASCADE, default=None)
    english_name = models.CharField(max_length=100)
    arabic_name = models.CharField(max_length=100)
    recipe_info_english = models.CharField(max_length=200, default=None)
    recipe_info_arabic = models.CharField(max_length=200, default=None)
    section = models.ForeignKey('Section', on_delete=models.CASCADE, default=None)
    meal_type = models.ForeignKey('MealType', on_delete=models.CASCADE, default=None)
    total_time = models.CharField(max_length=100, default=None)
    cooking_time = models.CharField(max_length=100, default=None)
    preparation_time = models.CharField(max_length=100, default=None)
    ingredient = models.ManyToManyField('Ingredient', null=True)
    sauce = models.ManyToManyField('Sauce')
    side_ingredients1 = models.CharField(max_length=200, default=None)
    side_ingredients2 = models.CharField(max_length=200, default=None)
    steps = models.ManyToManyField('Step')
    price = models.CharField(max_length=100, choices=PRICE_CHOICES, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.english_name
