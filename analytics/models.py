# analytics/models.py
from django.db import models

class AnalyticsBoard(models.Model):
    class Meta:
        managed = False
        app_label = "analytics"
        verbose_name = "Analytics"
        verbose_name_plural = "Analytics"

    def __str__(self):
        return "Google Analytics"

class FacebookBoard(models.Model):
    class Meta:
        managed = False
        app_label = "analytics"
        verbose_name = "Facebook"
        verbose_name_plural = "Facebook"

    def __str__(self):
        return "Facebook"
