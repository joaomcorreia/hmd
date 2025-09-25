from django.http import JsonResponse
from django.core.cache import cache
from django.utils import timezone

def ga_summary(request):
    key = "ga_summary_v1"
    data = cache.get(key)
    if not data:
        # STUB DATA — replace later with GA4 API result
        data = {
            "generated_at": timezone.now().isoformat(),
            "cards": [
                {"title": "Users (7d)", "value": 421},
                {"title": "Sessions (7d)", "value": 613},
                {"title": "Bounce Rate", "value": "47%"},
                {"title": "Top Page", "value": "/diensten/"},
            ],
        }
        cache.set(key, data, 120)  # 2 minutes for GA
    return JsonResponse(data)

def fb_summary(request):
    key = "fb_summary_v1"
    data = cache.get(key)
    if not data:
        # STUB DATA — replace later with Graph API result
        data = {
            "generated_at": timezone.now().isoformat(),
            "cards": [
                {"title": "Page Likes (28d)", "value": 37},
                {"title": "Post Reach (7d)", "value": 1803},
                {"title": "Messages (7d)", "value": 12},
                {"title": "Best Post", "value": "Keuken renovatie"},
            ],
        }
        cache.set(key, data, 900)  # 15 minutes for FB
    return JsonResponse(data)
