from django.contrib import admin
from .models import Section, Type, Kitchen, MealType, Unit, Recipe, Ingredient, Sauce, Step

admin.site.site_header = "Chef In Hand Admin"
admin.site.register(Section)
admin.site.register(Type)
admin.site.register(Kitchen)
admin.site.register(MealType)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Sauce)
admin.site.register(Step)

