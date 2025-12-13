from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustimUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
         ('Additional Info', {'fields': ('bio', 'profile_picture', 'followers')}),
     )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('bio', 'profile_picture', 'followers')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'count_followers')


    # def count_following(self, obj):
    #     return obj.count_following()
    # count_following.short_description = 'Folllowing Count'

    # def count_followers(self, obj):
    #     return obj.count_followers()
    # count_followers.short_descriptiom = 'Follower Count'

admin.site.register(CustomUser, CustimUserAdmin)