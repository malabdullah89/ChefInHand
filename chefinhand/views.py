from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required






@login_required
def home(request):
    return render(request, 'home.html', {})

@login_required
def addTaype(request):
    return render(request, 'add_type.html', {})

@login_required
def addSection(request):
    return render(request, 'add_section.html', {})

@login_required
def addIngredients(request):
    return render(request, 'add_ingredients.html', {})

@login_required
def addKitchen(request):
    return render(request, 'add_kitchen.html', {})

@login_required
def type_of_meal(request):
    return render(request, 'type_of_meal.html', {})

@login_required
def addUnite(request):
    return render(request, 'add_unit.html', {})

@login_required
def addUser(request):
    return render(request, 'add_user.html', {})


def chooseDashboard(request):
    return render(request, 'choose_page.html', {})

@login_required
def addProudect(request):
    return render(request, 'add_proudects.html', {})


@login_required
def addRecipe(request):
    return render(request, 'add_recipe.html', {})

@login_required
def chefDash(request):
    return render(request, 'chef_dash.html', {})

@login_required
def companyDash(request):
    return render(request, 'company_dash.html', {})

@login_required
def recipeList(request):
    return render(request, 'recipe_list.html', {})

@login_required
def addBook(request):
    return render(request, 'add_book.html', {})

@login_required
def userList(request):
    return render(request, 'user_list.html', {})

@login_required
def chefList(request):
    return render(request, 'chefs_list.html', {})

@login_required
def companyList(request):
    return render(request, 'company_list.html', {})

@login_required
def userStat(request):
    return render(request, 'users_stat.html', {})

@login_required
def chefStat(request):
    return render(request, 'chefs_stat.html', {})

@login_required
def companyStat(request):
    return render(request, 'company_stat.html', {})

@login_required
def totalRevenue(request):
    return render(request, 'total_revenue.html', {})

@login_required
def ChefsRevenue(request):
    return render(request, 'chefs_revenue.html', {})

@login_required
def chefBannerRevenue(request):
    return render(request, 'chefs_banners_revenue.html', {})

@login_required
def chefAddRecipe(request):
    return render(request, 'add_recipe_chef.html', {})

