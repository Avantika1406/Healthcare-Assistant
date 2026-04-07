import json
import requests

from django.shortcuts import render
from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .DiseasePredictor import predict_disease_simple
from .Translator import translate_text_safe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .ollamaAPI import ask_llm   #  Ollama wrapper
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.shortcuts import redirect

# ================= COMMON KEYWORDS =================

GREETINGS = [
    "hi", "hello", "hey", "hii", "heyy",
    "good morning", "good evening", "good afternoon"
]

SUICIDE_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "want to die",
    "hurt myself",
    "self harm",
    "attempt suicide"
]
# ================= HOME =================
def index(request):
    return render(request, "index.html")

    
def splash(request):
    return render(request, 'splash.html')


# ================= HEALTH CHAT =================
@csrf_exempt
def health_chat(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()
        

        if not message:
            return JsonResponse({
                "reply": "Please tell me what you’re feeling 🤍",
                "severity": "mild"
            })

        reply = ask_llm(message, mode="health")

        # basic severity (dummy but fine for project)
        severity = "mild"
        if any(word in message.lower() for word in ["severe", "unbearable", "emergency"]):
            severity = "severe"
        elif any(word in message.lower() for word in ["pain", "fever", "vomit", "weak"]):
            severity = "moderate"

        return JsonResponse({
            "reply": reply,
            "severity": severity
        })

    except Exception as e:
        print("HEALTH CHAT ERROR:", e)
        return JsonResponse({
            "reply": "I’m here to help 🤍 Please try again.",
            "severity": "mild"
        })


# ================= MENTAL CHAT =================
@csrf_exempt
def mental_chat(request):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()

        if not message:
            return JsonResponse({
                "reply": "I'm here with you 🤍"
            })

        message_lower = message.lower()

        if any(greet in message_lower for greet in GREETINGS):
            return JsonResponse({
                "reply": "Hey! 😊 How are you feeling today?"
            })

        if any(word in message_lower for word in SUICIDE_KEYWORDS):
            return JsonResponse({
                "reply": (
                    "I'm really sorry you're feeling this way. "
                    "You don't have to go through this alone. 💛\n\n"
                    "📞 Kiran Mental Health Helpline\n"
                    "1800-599-0019\n\n"
                    "📞 Tele-MANAS\n"
                    "14416\n\n"
                    "📞 AASRA Suicide Prevention Helpline\n"
                    "+91 22 2754 6669\n\n"
                    "I'm here to listen. What has been making things feel overwhelming?"
                )
            })

        reply = ask_llm(message, mode="mental")

        return JsonResponse({
            "reply": reply
        })

    except Exception as e:
        print("MENTAL CHAT ERROR:", e)

        return JsonResponse({
            "reply": "I'm here with you 🤍 Please try again."
        })

# ================= DIET CHAT =================
@csrf_exempt
def diet_chat(request):

    body = json.loads(request.body)
    message = body.get("message")

    reply = ask_llm(message, mode="diet")

    return JsonResponse({
        "reply": reply
    })


# ================= HEALTH SCORE =================
def get_health_score(request):
    # Dummy but frontend-compatible
    return JsonResponse({
        "total": 70,
        "bmi": 20,
        "mental": 20,
        "diet": 15,
        "consistency": 15
    })

@csrf_exempt
def disease_prediction_api(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        user_input = data.get("symptoms", "")

        result = predict_disease_simple(user_input)
        return JsonResponse(result)
    
# ================= LOGIN =================

def login_view(request):

    # if user already logged in
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        else:
            return render(request, "auth/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "auth/login.html")


from .models import UserProfile
@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    return render(request, "index.html", {
        "profile": profile
    })





def logout_view(request):
    logout(request)
    return redirect("splash")

# ================= PROFILE =================

@login_required
def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name")
        profile.age = request.POST.get("age")
        profile.gender = request.POST.get("gender")
        profile.language = request.POST.get("language")
        profile.save()
        return redirect("/profile/")

    return render(request, "profile.html", {"profile": profile})

# ================= UPDATE PROFILE =================

@login_required
def update_profile(request):
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)

        profile.age = request.POST["age"]
        profile.gender = request.POST["gender"]
        profile.height = request.POST["height"]
        profile.weight = request.POST["weight"]

        profile.save()

        return JsonResponse({"status": "ok"})
        return JsonResponse({"status": "ok"})


from .models import UserProfile

from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import UserProfile

# ================= SIGNUP =================
def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        age = int(request.POST.get("age") or 0)
        gender = request.POST.get("gender") or "Not set"
        height = int(request.POST.get("height") or 0)
        weight = int(request.POST.get("weight") or 0)

        if password != confirm:
            return render(request, "auth/signup.html", {
                "error": "Passwords do not match"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "auth/signup.html", {
                "error": "Username already exists"
            })

        user = User.objects.create_user(
            username=username,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            age=age,
            gender=gender,
            height=height,
            weight=weight
        )

        login(request, user)

        return redirect("dashboard")

    return render(request, "auth/signup.html")