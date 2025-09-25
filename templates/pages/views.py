from django.shortcuts import get_object_or_404, render
from .models import Page

def home(request):
    pg = Page.objects.filter(path="", is_published=True).first()
    if not pg:
        pg = Page(title="Home", body="<p>Welkom</p>")
    return render(request, "pages/page.html", {"page": pg})
