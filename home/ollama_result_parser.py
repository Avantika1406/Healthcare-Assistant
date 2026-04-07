import json
import re


class OllamaResultParser:

    @staticmethod
    def parse_result(result):
        try:
            result_json = json.loads(result)
            return result_json.get("response", "")
        except:
            return result


def extract_meal_lists(content):

    breakfast_list = []
    lunch_list = []
    evening_snack_list = []
    dinner_list = []
    exercises_list = []

    pattern = re.compile(r"<s>\s*(.*?)\s*<e>", re.DOTALL)

    matches = pattern.finditer(content)

    for match in matches:

        lines = match.group(1).strip().split("\n")

        if not lines:
            continue

        key = lines[0].strip()

        for line in lines[1:]:

            food = line.replace("-", "").strip()

            if key == "1. Breakfast":
                breakfast_list.append(food)

            elif key == "2. Lunch":
                lunch_list.append(food)

            elif key == "3. Evening Snack":
                evening_snack_list.append(food)

            elif key == "4. Dinner":
                dinner_list.append(food)

            elif key == "5. Exercises":
                exercises_list.append(food)

    return (
        breakfast_list,
        lunch_list,
        evening_snack_list,
        dinner_list,
        exercises_list
    )