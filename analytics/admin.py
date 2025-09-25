from django.contrib import admin
from django.template.response import TemplateResponse
from .models import AnalyticsBoard, FacebookBoard

@admin.register(AnalyticsBoard)
class AnalyticsBoardAdmin(admin.ModelAdmin):
    def has_add_permission(self, r): return False
    def has_change_permission(self, r, obj=None): return True
    def has_delete_permission(self, r, obj=None): return False
    def get_urls(self):
        urls = super().get_urls()
        return [*urls]  # keep default; page renders via changelist
    def changelist_view(self, request, extra_context=None):
        return TemplateResponse(request, "admin/analytics/board.html", {"title": "Google Analytics"})

@admin.register(FacebookBoard)
class FacebookBoardAdmin(admin.ModelAdmin):
    def has_add_permission(self, r): return False
    def has_change_permission(self, r, obj=None): return True
    def has_delete_permission(self, r, obj=None): return False
    def changelist_view(self, request, extra_context=None):
        return TemplateResponse(request, "admin/facebook/board.html", {"title": "Facebook"})
