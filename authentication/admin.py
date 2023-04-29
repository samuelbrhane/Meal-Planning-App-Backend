from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .models import UserAccount, UserGroups


class UserAccountAdmin(UserAdmin):
    ordering = ('email',)
    list_filter = UserAdmin.list_filter + ('groups__name',)
    list_display = ("id", "email","first_name","last_name","meal_type")
    list_display_links = ("id", "email","first_name")
    search_fields = ("first_name","last_name","email","allergies","meal_type")
    list_per_page = 25
    
    # super user permissions to delete user 
    def delete_user_and_tokens(self, request, queryset):
        for user in queryset:
            
            # Delete associated outstanding token
            outstanding_tokens = OutstandingToken.objects.filter(user=user)
            outstanding_tokens.delete()
            
            # Delete the user
            user.delete()
            
        self.message_user(request, "User and associated tokens deleted successfully.")
        
    delete_user_and_tokens.short_description = "Delete selected users and associated tokens"
    
    actions = [delete_user_and_tokens]


UserGroups.create_groups()
admin.site.register(UserAccount, UserAccountAdmin)
