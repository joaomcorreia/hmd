# core/admin.py
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import PasswordResetForm
from django.template.response import TemplateResponse
from django.db import models
from .models import Slide, PortfolioItem, SiteSettings, ContactSubmission

# Admin branding
admin.site.site_header = "HMD Klusbedrijf — Admin"
admin.site.site_title = "HMD Admin"
admin.site.index_title = "Beheer & overzicht"

# Hide Groups if unused
try:
    from django.contrib.auth.models import Group
    admin.site.unregister(Group)
except NotRegistered:
    pass

User = get_user_model()

# Unregister the default User admin so we can re-register
try:
    admin.site.unregister(User)
except NotRegistered:
    pass

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    actions = ["send_password_setup"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.exclude(is_superuser=True)
        return qs

    def get_readonly_fields(self, request, obj=None):
        base = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            return base + (
                "is_superuser",
                "is_staff",
                "user_permissions",
                "groups",
                "last_login",
                "date_joined",
            )
        return base

    def send_password_setup(self, request, queryset):
        sent = 0
        for user in queryset:
            if not user.email:
                continue
            form = PasswordResetForm({"email": user.email})
            if form.is_valid():
                form.save(
                    request=request,
                    use_https=request.is_secure(),
                    email_template_name="registration/password_reset_email.html",
                    subject_template_name="registration/password_reset_subject.txt",
                )
                sent += 1
        self.message_user(request, f"{sent} uitnodiging(en) verzonden.")

    send_password_setup.short_description = "Stuur wachtwoord-aanmaaklink"

# -------- Content models --------
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "order")
    list_editable = ("is_active", "order")
    search_fields = ("title", "subtitle")

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("title",)
    list_editable = ("is_active",)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("contact_email",)

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("name", "email", "phone", "message")

# -------- Static “Tools” pages in Admin (no DB, full sidebar) --------
class AdminStaticPage(models.Model):
    class Meta:
        managed = False
        app_label = "tools"
        default_permissions = ()

class Overview(AdminStaticPage):
    class Meta:
        proxy = True
        verbose_name = "Overview"
        verbose_name_plural = "Overview"

class DomainName(AdminStaticPage):
    class Meta:
        proxy = True
        verbose_name = "Domain Name"
        verbose_name_plural = "Domain Name"

class Hosting(AdminStaticPage):
    class Meta:
        proxy = True
        verbose_name = "Hosting"
        verbose_name_plural = "Hosting"

class Website(AdminStaticPage):
    class Meta:
        proxy = True
        verbose_name = "Website"
        verbose_name_plural = "Website"

class SEO(AdminStaticPage):
    class Meta:
        proxy = True
        verbose_name = "SEO"
        verbose_name_plural = "SEO"

class SocialNetworks(AdminStaticPage):
    class Meta:
        proxy = True
        verbose_name = "Social Networks"
        verbose_name_plural = "Social Networks"

class StaticPageAdmin(admin.ModelAdmin):
    change_list_template = None  # set per subclass

    # disable CRUD
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

    def changelist_view(self, request, extra_context=None):
        ctx = self.admin_site.each_context(request)  # gives full admin sidebar
        if extra_context:
            ctx.update(extra_context)
        return TemplateResponse(request, self.change_list_template, ctx)

@admin.register(Overview)
class OverviewAdmin(StaticPageAdmin):
    change_list_template = "admin/tools/overview.html"

@admin.register(DomainName)
class DomainNameAdmin(StaticPageAdmin):
    change_list_template = "admin/tools/domain-name.html"

@admin.register(Hosting)
class HostingAdmin(StaticPageAdmin):
    change_list_template = "admin/tools/hosting.html"

@admin.register(Website)
class WebsiteAdmin(StaticPageAdmin):
    change_list_template = "admin/tools/website.html"

@admin.register(SEO)
class SEOAdmin(StaticPageAdmin):
    change_list_template = "admin/tools/seo.html"

@admin.register(SocialNetworks)
class SocialNetworksAdmin(StaticPageAdmin):
    change_list_template = "admin/tools/social-networks.html"
