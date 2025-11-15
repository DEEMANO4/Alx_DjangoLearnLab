from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from.models import CustomUser, CustomUserManager

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publicatiion_year')
    search_fields = ('title', 'author', 'publication_year')

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_of_birth',)
    fieldsets = UserAdmin.fieldsets + (
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo',)})
    )

admin.site.register(Book, CustomUser, CustomUserAdmin)