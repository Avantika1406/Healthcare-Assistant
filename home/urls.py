from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path("app/", views.index, name="home"),

    path("health-chat/", views.health_chat),
    path("mental-chat/", views.mental_chat),
    path("diet-chat/", views.diet_chat),
    path("health-score/", views.get_health_score),

    path("profile/", views.profile_view),
    path("update-profile/", views.update_profile),
]