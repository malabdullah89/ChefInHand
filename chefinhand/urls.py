from django.contrib import admin
from django.urls import path, include

import contentsManagement.urls
from accounts.views import login_view, register_view, logout_view
from chefinhand.views import home, type_of_meal, addUnite, addUser, \
    chooseDashboard, addProudect, chefDash, companyDash, addBook, userList, chefList, \
    companyList, userStat, chefStat, companyStat, totalRevenue, ChefsRevenue, chefBannerRevenue
from contentsManagement.views import Sections, RecipesList, AddRecipe, DeleteRecipe, UpdateRecipe, AddTypes, AddIngredient, AddKitchen, AddMealType

urlpatterns = [
    path('', chooseDashboard),
    path('admin_dash', home),
    path('chef_dash', chefDash),
    path('company_dash', companyDash),
    path('admin_dash/add_type', AddTypes.as_view()),
    path('admin_dash/user_list', userList),
    path('admin_dash/chef_list', chefList),
    path('admin_dash/company_list', companyList),
    path('admin_dash/user_stat', userStat),
    path('admin_dash/chef_stat', chefStat),
    path('admin_dash/company_stat', companyStat),
    path('admin_dash/total_revenue', totalRevenue),
    path('admin_dash/chefs_revenue', ChefsRevenue),
    path('admin_dash/chefs_banners_revenue', chefBannerRevenue),
    path('admin_dash/add_section', Sections.as_view()),
    path('admin_dash/add_ingredients', AddIngredient.as_view()),
    path('admin_dash/add_proudects', addProudect),
    path('admin_dash/add_book', addBook),
    path('admin_dash/add_kitchen', AddKitchen.as_view()),
    path('admin_dash/add_recipe', AddRecipe.as_view()),
    path('admin_dash/recipe_list', RecipesList.as_view()),
    path('admin_dash/add_user', addUser),
    path('admin_dash/type_of_meal', AddMealType.as_view()),
    path('admin_dash/add_unite', addUnite),
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view),
    path('admin_dash/delete/<slug:pk>', DeleteRecipe.as_view(), name='delete_recipe'),
    path('admin_dash/update/<slug:pk>', UpdateRecipe.as_view(), name='update_recipe'),

]
