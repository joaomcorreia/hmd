from django.db import models

# --- Slider ---
class Slide(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='slider/')
    cta1_label = models.CharField(max_length=40, blank=True)
    cta1_url = models.URLField(blank=True)
    cta2_label = models.CharField(max_length=40, blank=True)
    cta2_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.order} · {self.title}"


# --- Portfolio (single, canonical definition) ---
class PortfolioItem(models.Model):
    # choices used by admin forms
    CAT_CHOICES = [
        ("1", "Keuken"),
        ("2", "Badkamer"),
        ("3", "Vloeren"),
        ("4", "Kluswerk Algemeen"),
        ("5", "Klus en Reparatiewerk"),
        ("6", "Timmerwerk"),
        ("7", "Elektrisch Werk"),
        ("8", "Loodgieterij"),
        ("9", "Stukwerk"),
    ]

    # map to URL/CSS slugs
    SLUGS = {
        "1": "keuken",
        "2": "badkamer",
        "3": "vloeren",
        "4": "kluswerk-algemeen",
        "5": "klus-en-reparatiewerk",
        "6": "timmerwerk",
        "7": "elektrisch-werk",
        "8": "loodgieterij",
        "9": "stukwerk",
    }

    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to="portfolio/")
    category = models.CharField(max_length=2, choices=CAT_CHOICES)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created"]

    def __str__(self):
        return self.title or f"Item {self.pk}"

    @property
    def category_slug(self) -> str:
        return self.SLUGS.get(self.category, "overig")


# --- Core / site ---
class SiteSettings(models.Model):
    contact_email = models.EmailField(default="justcodeworks@gmail.com")
    whatsapp = models.CharField(max_length=32, blank=True, default="+31687111289")
    phone_display = models.CharField(max_length=32, blank=True, default="06 87111289")

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return "Site settings"


class ContactSubmission(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} • {self.created_at:%Y-%m-%d %H:%M}"


# --- Facebook integration ---
class FacebookSettings(models.Model):
    page_id = models.CharField(max_length=64, blank=True)
    page_name = models.CharField(max_length=255, blank=True)
    ad_account_id = models.CharField(max_length=64, blank=True)
    app_id = models.CharField(max_length=64, blank=True)
    app_secret = models.CharField(max_length=128, blank=True)
    user_access_token = models.TextField(blank=True)      # short-lived
    page_access_token = models.TextField(blank=True)      # long-lived
    token_expires = models.DateTimeField(null=True, blank=True)
    connected = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Facebook settings"
        verbose_name_plural = "Facebook settings"

    def __str__(self):
        return "Facebook settings"


class FacebookPost(models.Model):
    page_post_id = models.CharField(max_length=128, unique=True)  # {page_id}_{post_id}
    created_time = models.DateTimeField()
    message = models.TextField(blank=True)
    permalink = models.URLField(max_length=500, blank=True)
    media_url = models.URLField(max_length=500, blank=True)
    reactions = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_time"]


class FacebookLead(models.Model):
    lead_id = models.CharField(max_length=64, unique=True)
    form_id = models.CharField(max_length=64)
    created_time = models.DateTimeField()
    data = models.JSONField()
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_time"]


class FacebookCampaign(models.Model):
    campaign_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    daily_budget = models.IntegerField(null=True, blank=True)  # cents
    objective = models.CharField(max_length=64, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_stop = models.DateField(null=True, blank=True)
    spend = models.FloatField(default=0.0)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
