from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Page

def home(request):
    # Try DB Home page, else simple OK
    pg = Page.objects.filter(path="", is_published=True).first()
    if pg:
        return render(request, "pages/page.html", {"page": pg})
    return HttpResponse("OK")

def page_by_path(request, path=""):
    norm = (path or "").strip("/")
    page = get_object_or_404(Page, path=norm, is_published=True)
    return render(request, "pages/page.html", {"page": page})
