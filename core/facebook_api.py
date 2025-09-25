import requests
from django.conf import settings
from .models import FacebookSettings

GRAPH = "https://graph.facebook.com/v19.0"

def _token():
    s = FacebookSettings.objects.first()
    return s.page_access_token if s and s.page_access_token else None

def get_page_posts(limit=25):
    s = FacebookSettings.objects.first()
    if not s or not s.page_id or not _token(): return []
    fields = "id,created_time,message,permalink_url,full_picture,shares.summary(true),comments.summary(true),reactions.summary(true)"
    url = f"{GRAPH}/{s.page_id}/posts"
    r = requests.get(url, params={"fields": fields, "limit": limit, "access_token": _token()}, timeout=20)
    r.raise_for_status()
    return r.json().get("data", [])

def get_campaigns():
    s = FacebookSettings.objects.first()
    if not s or not s.ad_account_id or not _token(): return []
    url = f"{GRAPH}/act_{s.ad_account_id}/campaigns"
    fields = "id,name,status,objective,start_time,stop_time,daily_budget"
    r = requests.get(url, params={"fields": fields, "access_token": _token()}, timeout=20)
    r.raise_for_status()
    return r.json().get("data", [])

def get_campaign_insights(campaign_id):
    url = f"{GRAPH}/{campaign_id}/insights"
    r = requests.get(url, params={"fields":"spend,impressions,clicks", "access_token": _token()}, timeout=20)
    r.raise_for_status()
    d = r.json().get("data", [])
    return d[0] if d else {}
