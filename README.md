a# 🏥 Healthcare Assistant

An AI-powered Healthcare Assistant web application built using Django and Machine Learning. This system helps users predict possible diseases based on symptoms, interact with an intelligent chatbot, and manage their health data efficiently.

---

## 🚀 Features

* 🤖 AI Chatbot for healthcare assistance
* 🧠 Disease Prediction using Machine Learning models
* 🌐 Multi-language support (Hindi, Marathi, English)
* 📊 User Dashboard for health insights
* 🔐 User Authentication (Login/Signup)
* 📁 Structured backend with Django

---

## 🛠️ Tech Stack

**Frontend:**

* HTML
* CSS

**Backend:**

* Python (Django)

**Machine Learning:**

* Scikit-learn
* Decision Tree, Random Forest, Gradient Boosting, Naive Bayes

**Database:**

* SQLite

**Other Tools:**

* Ollama API / LLM integration
* Git & GitHub

---

## 📂 Project Structure

```
Healthcare-Assistant/
│── chatbot/              # Main Django project
│── home/                 # Core app (views, models, ML logic)
│── dataset/              # Dataset for training/testing
│── model/                # Trained ML models (.joblib)
│── templates/            # HTML templates
│── static/               # CSS files
│── locale/               # Multi-language support
│── manage.py             # Django entry point
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Avantika1406/Healthcare-Assistant.git
cd Healthcare-Assistant
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add environment variables

Create a `.env` file in root:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the server

```bash
python manage.py runserver
```

👉 Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 How It Works

* User enters symptoms
* Machine learning models analyze input
* System predicts possible diseases
* Chatbot provides additional guidance
* Data stored and shown in dashboard

---

## 🔐 Security Note

* API keys are stored in `.env` file
* `.env` is ignored using `.gitignore`
* Never expose sensitive credentials publicly

---

## 📸 Screenshots

*Add your project screenshots here (UI, dashboard, chatbot, etc.)*

---

## 📈 Future Improvements

* 🌍 Deployment (AWS / Render / Vercel)
* 📱 Mobile responsive UI
* 🧾 Medical report generation
* 🔔 Real-time alerts & notifications

---

## 👩‍💻 Author

**Avantika Pawar**

* GitHub: https://github.com/Avantika1406

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 💬 Share feedback

---

## 📜 License

This project is for educational purposes.
