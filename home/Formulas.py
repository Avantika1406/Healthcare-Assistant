from decimal import Decimal, ROUND_DOWN
from datetime import datetime


# ===============================
# AGE CALCULATION
# ===============================
def calculate_age(birth_year):
    return datetime.now().year - int(birth_year)


# ===============================
# TDEE CALCULATION
# ===============================
def TDEE(age, weight, height, gender, activity_level):
    age = float(age)
    height = float(height)
    weight = float(weight)

    gender = gender.lower()
    activity_level = activity_level.lower()

    # BMR Calculation
    if gender == "female":
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    else:
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

    # Activity multiplier
    if activity_level == "sedentary":
        tdee = bmr * 1.2
    elif activity_level == "lightly active":
        tdee = bmr * 1.375
    elif activity_level == "moderately active":
        tdee = bmr * 1.55
    elif activity_level == "very active":
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.55  # default safe value

    return str(Decimal(tdee).quantize(Decimal("0"), rounding=ROUND_DOWN))


# ===============================
# DIET PROMPT GENERATOR
# ===============================
def generate_formatted_string(user_dict):

    # Extract user data
    selected_diseases = user_dict.get("selectedDiseases", "")
    user_profession = user_dict.get("userProfession", "")
    user_vegetarian = user_dict.get("userVegetarian", "")
    user_activity_level = user_dict.get("useractivitylevel", "")
    user_birth_year = user_dict.get("userbyear", "")
    user_current_weight = user_dict.get("usercurrentweight", "")
    user_gender = user_dict.get("usergender", "")
    user_height = user_dict.get("userheight", "")
    selected_allergies = user_dict.get("selectedAllergies", "")
    selected_weight_goal = user_dict.get("selectedWeightGoal", "")

    # Calculate TDEE
    user_age = calculate_age(user_birth_year)
    user_tdee = TDEE(
        user_age,
        user_current_weight,
        user_height,
        user_gender,
        user_activity_level,
    )

    # Vegetarian formatting
    if user_vegetarian.lower() == "yes":
        user_vegetarian = "YES (Pure Vegetarian, no eggs)"
    else:
        user_vegetarian = "Non-vegetarian (includes eggs & chicken)"

    # Diseases & allergies formatting
    selected_diseases = (
        f"Diseases Suffering: {selected_diseases}"
        if selected_diseases
        else "No known diseases"
    )

    selected_allergies = (
        f"I have allergies to: {selected_allergies}"
        if selected_allergies
        else "No known allergies"
    )

    # Final AI prompt
    formatted_string = f"""
Please generate an Indian diet plan using Indian food based on the following details:

Age: {user_age}
Gender: {user_gender}
Height: {user_height} cm
Weight: {user_current_weight} kg
Activity Level: {user_activity_level}
Weight Goal: {selected_weight_goal}
{selected_allergies}
Vegetarian Status: {user_vegetarian}
Profession: {user_profession}
{selected_diseases}
Max Calories: {user_tdee} kcal

Please keep the output format exactly as below:

<s>
1. Breakfast
.. meal info with calories & nutrition
<e>

<s>
2. Lunch
.. meal info with calories & nutrition
<e>

<s>
3. Evening Snack
.. meal info with calories & nutrition
<e>

<s>
4. Dinner
.. meal info with calories & nutrition
<e>

<s>
5. Exercises
.. simple exercises based on health & profession
<e>

Rules:
- Do NOT diagnose
- Respect allergies and diseases
- Ensure total calories stay within the limit
- Keep suggestions practical and Indian
"""

    return formatted_string


# ===============================
# TEST RUN (OPTIONAL)
# ===============================
if __name__ == "__main__":
    user_dict = {
        "selectedDiseases": "Diabetes",
        "userProfession": "Software Engineer",
        "userVegetarian": "No",
        "useractivitylevel": "Moderately Active",
        "userbyear": "2000",
        "usercurrentweight": "70",
        "usergender": "Male",
        "userheight": "170",
        "selectedAllergies": "Peanuts",
        "selectedWeightGoal": "Lose Weight",
    }
    print(generate_formatted_string(user_dict))

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 18.5:
        return bmi, "Underweight", "Low"
    elif bmi < 25:
        return bmi, "Normal", "Low"
    elif bmi < 30:
        return bmi, "Overweight", "Medium"
    else:
        return bmi, "Obese", "High"


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)
