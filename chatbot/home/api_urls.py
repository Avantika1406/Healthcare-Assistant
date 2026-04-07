from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("get-chat-history/", get_chat_history),
path("save-settings/", save_settings),
path("get-settings/", get_settings),
]
