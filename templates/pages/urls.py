from django.contrib import admin
from django.urls import path
from pages.views import page_by_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", page_by_path, name="home"),                   # '' -> home page
    path("<path:path>/", page_by_path, name="page"),       # nested paths
]
