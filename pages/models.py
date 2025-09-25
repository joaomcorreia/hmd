from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=150)
    path = models.CharField(max_length=255, unique=True, blank=True)
    body = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    menu_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["menu_order", "title"]

    def clean(self):
        self.path = (self.path or "").strip("/")

    def __str__(self):
        return self.title
