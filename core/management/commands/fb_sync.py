from django.core.management.base import BaseCommand
from core.facebook_api import get_page_posts, get_campaigns, get_campaign_insights
from core.models import FacebookPost, FacebookCampaign
from datetime import datetime

class Command(BaseCommand):
    help = "Sync Facebook posts and campaigns"

    def handle(self, *args, **opts):
        # posts
        for p in get_page_posts(limit=50):
            pid = p["id"]
            post, _ = FacebookPost.objects.update_or_create(
                page_post_id=pid,
                defaults={
                    "created_time": datetime.fromisoformat(p["created_time"].replace("Z","+00:00")),
                    "message": p.get("message",""),
                    "permalink": p.get("permalink_url",""),
                    "media_url": p.get("full_picture",""),
                    "reactions": p.get("reactions",{}).get("summary",{}).get("total_count",0),
                    "comments": p.get("comments",{}).get("summary",{}).get("total_count",0),
                    "shares": p.get("shares",{}).get("count",0),
                }
            )
        # campaigns + insights
        for c in get_campaigns():
            ins = get_campaign_insights(c["id"]) or {}
            FacebookCampaign.objects.update_or_create(
                campaign_id=c["id"],
                defaults={
                    "name": c.get("name",""),
                    "status": c.get("status",""),
                    "objective": c.get("objective",""),
                    "daily_budget": int(c.get("daily_budget") or 0),
                    "spend": float(ins.get("spend",0)),
                    "impressions": int(ins.get("impressions",0)),
                    "clicks": int(ins.get("clicks",0)),
                }
            )
