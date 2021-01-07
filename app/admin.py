from django.contrib import admin
from app.models import customUser,Blog
# Register your models here.

class adminCustomUser(admin.ModelAdmin):
    list_display = ['email','name']

class CustomBlog(admin.ModelAdmin):
    list_display = ['title','created_at','author']
admin.site.register(customUser,adminCustomUser)
admin.site.register(Blog,CustomBlog)
