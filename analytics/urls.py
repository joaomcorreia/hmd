from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import ga_summary, fb_summary

urlpatterns = [
    path("admin/api/ga/summary/", staff_member_required(ga_summary), name="ga_summary"),
    path("admin/api/fb/summary/", staff_member_required(fb_summary), name="fb_summary"),
]
