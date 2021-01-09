from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Customer, Chef, Company

admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Chef)
admin.site.register(Company)

