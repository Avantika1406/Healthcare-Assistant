import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "dataset.xlsx")

def predict_disease_simple(symptoms):
    # Temporary safe fallback
    if not os.path.exists(DATASET_PATH):
        return "Disease prediction model not configured yet"

    try:
        df = pd.read_excel(DATASET_PATH)
        return "Disease prediction connected (dataset loaded)"
    except Exception:
        return "Error loading disease dataset"
