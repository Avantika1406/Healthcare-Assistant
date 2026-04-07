from django.urls import path
from .views import get_chat_history


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),   # 👈 THIS LINE FIXES EVERYTHING
]
