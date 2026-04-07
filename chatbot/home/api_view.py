from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.DiseasePredictor import predict_disease_from_symptom
from home.ollamaAPI import ChatGPTApi


# 🔹 CHATBOT API
@api_view(['POST'])
def chat_api(request):
    message = request.data.get("message")

    if not message:
        return Response({"error": "Message is required"}, status=400)

    reply = ChatGPTApi.run(message)

    return Response({
        "user_message": message,
        "bot_reply": reply
    })


# 🔹 BMI API
@api_view(['POST'])
def bmi_api(request):
    try:
        height = float(request.data.get("height"))
        weight = float(request.data.get("weight"))

        bmi = round(weight / ((height / 100) ** 2), 2)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        return Response({
            "bmi": bmi,
            "status": status
        })

    except:
        return Response({"error": "Invalid input"}, status=400)


# 🔹 DISEASE PREDICTION API
@api_view(['POST'])
def disease_api(request):
    symptoms = request.data.get("symptoms")

    if not symptoms:
        return Response({"error": "Symptoms required"}, status=400)

    disease, dtype = predict_disease_from_symptom(symptoms)

    return Response({
        "predicted_disease": disease,
        "type": dtype
    })
