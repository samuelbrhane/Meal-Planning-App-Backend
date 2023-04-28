from django.contrib import admin
from .models import UserAccount, UserGroups
from django.contrib.auth.admin import UserAdmin


class UserAccountAdmin(admin.ModelAdmin):
    list_filter = UserAdmin.list_filter + ('groups__name',)
    list_display = ("id", "email","first_name","last_name","meal_type")
    list_display_links = ("id", "email","first_name")
    search_fields = ("first_name","last_name","email","allergies","meal_type")
    list_per_page = 25
    
UserGroups.create_groups()

admin.site.register(UserAccount, UserAccountAdmin)
