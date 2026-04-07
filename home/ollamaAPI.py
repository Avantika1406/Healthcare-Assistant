
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "mistral:7b-instruct"


def ask_llm(message, mode="health", extra_prompt=None):
    msg = message.lower().strip()

    # -------- Greeting handling --------
    if msg in ["hi", "hello", "hey", "hii"]:
        return (
            "Hello 👋 I'm your Healthcare Assistant.\n"
            "How are you feeling today?\n"
            "You can tell me about any symptoms you're experiencing."
        )

    try:

        # ---------------- HEALTH MODE ----------------
        if mode == "health":
            system_prompt = (
                "You are a friendly and practical doctor.\n"
                    "Rules:\n"
                    "- Be direct and helpful.\n"
                    "- Give medicine when asked.\n"
                    "- Keep it 2–3 sentences only.\n"
                    "- Use natural human tone.\n"
                    "- Slightly personalize based on user input.\n"
                    "- Avoid repeating the same phrases.\n"
                    "- End with 1 short question.\n"
            )

        # ---------------- MENTAL MODE ----------------
        elif mode == "mental":
            system_prompt = (
                "You are a warm and empathetic therapist having a conversation with someone.\n"
                "Respond like a real human therapist, not an AI.\n"
                "Start by acknowledging their feelings.\n"
                "Use supportive phrases like 'I hear you' or 'that sounds really hard'.\n"
                "Keep the reply 2–3 sentences.\n"
                "Be gentle and understanding.\n"
                "End with one thoughtful open question."
            )

        # ---------------- DIET MODE ----------------
        elif mode == "diet":
            system_prompt = (
                "You are an Indian diet planner.\n"
        "Give simple diet plans.\n\n"

        "Rules:\n"
        "- ONLY give 4 sections:\n"
        "Breakfast, Lunch, Snack, Dinner\n"
        "- Each section: max 3 items\n"
        "- Use bullet points (-)\n"
        "- No explanation\n"
        "- Keep it clean and short\n\n"

        "Example:\n"
        "Breakfast:\n"
        "- Eggs\n"
        "- Toast\n\n"
        "Lunch:\n"
        "- Rice\n"
        "- Dal\n\n"
        "Snack:\n"
        "- Fruits\n\n"
        "Dinner:\n"
        "- Roti\n"
        "- Sabzi\n"
            )

        else:
            system_prompt = "You are a helpful assistant."

        if extra_prompt:
            system_prompt += "\n" + extra_prompt

        prompt = f"""
{system_prompt}

Patient says:
{message}

Reply naturally to the patient.
"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
    "temperature": 0.6,
    "top_p": 0.9,
    "num_predict": 300,
    "repeat_penalty": 1.2
}
            },
            timeout=60
        )

        data = response.json()

        # -------- Clean model output --------
        reply = data.get("response", "I'm here to help.")
        reply = reply.replace("-----", "")
        reply = reply.replace("\n\n", "\n")
        reply = reply.strip().strip('"')

        return reply

    except Exception as e:
        print("OLLAMA ERROR:", e)
        return "I'm here with you 🤍"