from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserCategory, UserChangeForm
from .models import Users

class CustomUser(UserAdmin):
    add_form = UserCategory
    form = UserChangeForm
    model = Users
    list_display = ['id','name', 'description']

admin.site.register(Users, CustomUser)