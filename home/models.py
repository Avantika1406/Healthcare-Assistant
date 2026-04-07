from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class ChatMessage(models.Model):
    ROLE_CHOICES = (
        ("user", "User"),
        ("ai", "AI"),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.role}: {self.content[:30]}"


class ChatHistory(models.Model):
    MODE_CHOICES = [
        ("health", "Health"),
        ("mental", "Mental"),
        ("diet", "Diet"),
    ]

    user_message = models.TextField()
    ai_reply = models.TextField()
    mode = models.CharField(max_length=20, choices=MODE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mode} - {self.created_at}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    language = models.CharField(max_length=20, default="English")

    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class AppSettings(models.Model):
    auto_scroll = models.BooleanField(default=True)
    mental_reminders = models.BooleanField(default=False)
    theme = models.CharField(max_length=20, default="light")
    language = models.CharField(max_length=20, default="en")
    save_chat_history = models.BooleanField(default=True)
    save_health_journey = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "App Settings"


class JournalEntry(models.Model):
    question = models.TextField()
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:30]


class HealthScore(models.Model):
    bmi_score = models.IntegerField(default=0)
    mental_score = models.IntegerField(default=0)
    diet_score = models.IntegerField(default=0)
    consistency_score = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)


class HealthScoreHistory(models.Model):
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.score}"