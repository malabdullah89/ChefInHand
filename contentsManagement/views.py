from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, FormView, DeleteView, UpdateView
from chefinhand.views import home
from .models import Section, Recipe, Type, Ingredient, Kitchen, MealType
from .forms import AddSection, AddRecipe, UpdateRecipe, AddType, AddIngredientForm, AddKitchenForm, AddMealTypeForm


class Sections(TemplateView):  # Section Page
    template_name = 'add_section.html'

    def get(self, request):
        sections = Section.objects.filter(created_by_id=request.user)  # Sections List based on user logged in
        form = AddSection(request.POST)
        context = {'sections': sections, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddSection(request.POST)
        if form.is_valid():
            form.instance.created_by = self.request.user
            form.save()

            return redirect('./add_section')
        return render(request, self.template_name, {'form': form})


class RecipesList(TemplateView):
    template_name = 'recipe_list.html'

    def get(self, request):
        recipes = Recipe.objects.filter(created_by_id=request.user)  # Query to view Recipes based on user logged in

        context = {'recipes': recipes}
        return render(request, self.template_name, context)


class AddRecipe(SuccessMessageMixin, FormView):  # Add Recipe Form in Chef Dashbaord
    template_name = 'add_recipe.html'
    form_class = AddRecipe
    success_message = "created successfully"

    def form_valid(self, form):
        if form.is_valid():
            form.instance.created_by = self.request.user  # Add Recipe based on User logged in
            form.save()

            return redirect('./add_recipe')
        return super(AddRecipe, self).form_valid(form)


class DeleteRecipe(DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy(home)


class UpdateRecipe(UpdateView):
    model = Recipe
    template_name_suffix = '_update_form'
    template_name = 'update_recipe.html'
    form_class = UpdateRecipe
    success_url = reverse_lazy(home)


class AddTypes(TemplateView):  # Section Page
    template_name = 'add_type.html'

    def get(self, request):
        types = Type.objects.all()
        form = AddType(request.POST)
        context = {'types': types, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddType(request.POST)
        if form.is_valid():
            form.instance.created_by = self.request.user
            form.save()

            return redirect('./add_type')
        return render(request, self.template_name, {'form': form})


class AddIngredient(TemplateView):  # Section Page
    template_name = 'add_ingredients.html'

    def get(self, request):
        ingredients = Ingredient.objects.all  # Sections List based on user logged in
        form = AddIngredientForm(request.POST)
        context = {'ingredients': ingredients, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddIngredientForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('./add_ingredients')
        return render(request, self.template_name, {'form': form})


class AddKitchen(TemplateView):
    template_name = 'add_kitchen.html'

    def get(self, request):
        kitchens = Kitchen.objects.filter(created_by_id=request.user)
        form = AddKitchenForm(request.POST)
        context = {'kitchens': kitchens, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddKitchenForm(request.POST)
        if form.is_valid():
            form.instance.created_by = self.request.user
            form.save()

            return redirect('./add_kitchen')
        return render(request, self.template_name, {'form': form})


class AddMealType(TemplateView):
    template_name = 'type_of_meal.html'

    def get(self, request):
        meal_types = MealType.objects.all()
        form = AddMealTypeForm(request.POST)
        context = {'meal_types': meal_types, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AddMealTypeForm(request.POST)
        if form.is_valid():
            form.instance.created_by = self.request.user
            form.save()

            return redirect('./type_of_meal')
        return render(request, self.template_name, {'form': form})
