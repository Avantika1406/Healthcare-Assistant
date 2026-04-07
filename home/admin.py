from django.contrib import admin
from .models import ChatMessage, ChatHistory, UserProfile, AppSettings

admin.site.register(UserProfile)
admin.site.register(ChatMessage)
admin.site.register(ChatHistory)
admin.site.register(AppSettings)
