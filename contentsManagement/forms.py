from django import forms

from accounts.models import Chef
from . import models
from .models import Type, Kitchen, Section, MealType, Ingredient, Sauce, Recipe

PRICE_CHOICES = (
    ('Free', 'Free'),
    ('$1', '$1'),
    ('$2', '$2'),
    ('$3', '$3'),
    ('$4', '$4'),
    ('$5', '$5')

)


class AddSection(forms.ModelForm):
    section_english_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type English Name',

        }
    ))
    section_arabic_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Arabic Name',

        }
    ))

    class Meta:
        model = models.Section
        exclude = ['created_by', ]


class AddRecipe(forms.ModelForm):
    chef_name = forms.ModelChoiceField(queryset=Chef.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',

        }
    ))

    kitchen_type = forms.ModelChoiceField(queryset=Kitchen.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    english_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    arabic_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    recipe_info_english = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    recipe_info_arabic = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    section = forms.ModelChoiceField(queryset=Section.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    meal_type = forms.ModelChoiceField(queryset=MealType.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    total_time = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    cooking_time = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    preparation_time = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    sauce = forms.ModelChoiceField(queryset=Sauce.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    side_ingredients1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    side_ingredients2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    steps = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    price = forms.ChoiceField(choices=PRICE_CHOICES, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = models.Recipe
        fields = [
            'chef_name',
            'kitchen_type',
            'english_name',
            'arabic_name',
            'recipe_info_english',
            'recipe_info_arabic',
            'section',
            'meal_type',
            'total_time',
            'cooking_time',
            'preparation_time',
            'ingredient',
            'sauce',
            'side_ingredients1',
            'side_ingredients2',
            'steps',
            'price'

        ]


class UpdateRecipe(forms.ModelForm):
    english_name = forms.CharField(label='English Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type English Name'

        }
    ))
    arabic_name = forms.CharField(label='Arabic Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Arabic Name',
        }
    ))
    choose_type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type', widget=forms.Select(
        attrs={
            'class': 'form-control',

        }
    ))
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Company Name',
        }
    ))
    barcode = forms.CharField(label='Barcode No.', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Barcode No.',
        }
    ))

    class Meta:
        model = models.Recipe
        fields = [
            'english_name',
            'arabic_name',
            'choose_type',
            'company_name',
            'barcode',

        ]


class AddType(forms.ModelForm):
    type_english_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type English Name',

        }
    ))
    type_arabic_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Arabic Name',

        }
    ))

    class Meta:
        model = models.Type
        fields = [
            'type_english_name',
            'type_arabic_name',

        ]


class AddIngredientForm(forms.ModelForm):
    proudect_english_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))
    proudect_arabic_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))

    barcode_number = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))

    proudect_company_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',

        }
    ))

    class Meta:
        model = models.Type
        fields = [
            'proudect_english_name',
            'proudect_arabic_name',
            'barcode_number',
            'proudect_company_name',

        ]


class AddKitchenForm(forms.ModelForm):
    english_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type English Name',

        }
    ))
    arabic_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Arabic Name',

        }
    ))

    class Meta:
        model = models.Kitchen
        exclude = ['created_by', ]


class AddMealTypeForm(forms.ModelForm):
    english_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type English Name',

        }
    ))
    arabic_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type Arabic Name',

        }
    ))

    class Meta:
        model = models.MealType
        exclude = ['created_by', ]
