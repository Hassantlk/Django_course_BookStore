from dataclasses import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser

    # اضافه کردن فیلدهای جدید به صفحه ی مشاهده یوزرها
    # در صفحه admin
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", )}),
    )
    # اضافه کردن فیلدهای جدید به هنگام اد کردن یوزر جدید
    # در صفحه admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age", )}),
    )
    #-------------------------------
    list_display = ["username", "email", "age", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)

