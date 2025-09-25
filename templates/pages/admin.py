# pages/admin.py
from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title","path","is_published","menu_order")
    search_fields = ("title","path","body")
    list_filter = ("is_published",)
