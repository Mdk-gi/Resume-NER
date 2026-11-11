
from pathlib import Path
import os
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    pipeline
)

# =====================================
# 1. MODEL CONFIGURATION
# =====================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

LOCAL_MODEL_PATH = PROJECT_ROOT / "models" / "p30_bert_final"

# Replace with your Hugging Face model ID
HF_MODEL_ID = "YOUR-USERNAME/p30-resume-ner-model"

# =====================================
# 2. DEVICE
# =====================================

device = 0 if torch.cuda.is_available() else -1

print("Loading trained resume NER model...")
print("Device:", "GPU" if device == 0 else "CPU")

# =====================================
# 3. LOAD MODEL
# =====================================

if LOCAL_MODEL_PATH.exists() and (
    LOCAL_MODEL_PATH / "model.safetensors"
).exists():

    print("Loading model from local folder...")

    MODEL_SOURCE = str(LOCAL_MODEL_PATH)
    LOCAL_ONLY = True

else:

    print("Downloading trained model from Hugging Face...")

    MODEL_SOURCE = HF_MODEL_ID
    LOCAL_ONLY = False

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_SOURCE,
    local_files_only=LOCAL_ONLY
)

model = AutoModelForTokenClassification.from_pretrained(
    MODEL_SOURCE,
    local_files_only=LOCAL_ONLY
)

print("Trained model loaded successfully!")

# =====================================
# 4. CREATE PIPELINE
# =====================================

ner_pipeline = pipeline(
    task="token-classification",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
    device=device
)

# =====================================
# 5. ENTITY LABELS
# =====================================

ENTITY_LABELS = [
    "NAME",
    "EMAIL",
    "PHONE",
    "SKILL",
    "DEGREE",
    "COLLEGE",
    "COMPANY",
    "DESIGNATION",
    "EXPERIENCE",
    "LOCATION",
    "GRADUATION_YEAR",
    "CERTIFICATION"
]

# =====================================
# 6. ENTITY EXTRACTION
# =====================================

def extract_entities(text):

    if not isinstance(text, str) or not text.strip():
        return {}

    predictions = ner_pipeline(text)

    results = {label: [] for label in ENTITY_LABELS}

    for item in predictions:

        entity = item["entity_group"]
        value = item["word"].strip()

        if entity in results and value:
            if value not in results[entity]:
                results[entity].append(value)

    return {
        entity: values
        for entity, values in results.items()
        if values
    }


# =====================================
# 7. TEST
# =====================================

if __name__ == "__main__":

    sample_text = """
    Mohammed Kurupkar
    Email: mohammed@gmail.com
    Phone: 9876543210

    B.Tech Computer Science
    MIT ADT University

    Skills: Python, Machine Learning, SQL
    Location: Pune
    """

    print("\nExtracting entities...\n")

    output = extract_entities(sample_text)

    for entity, values in output.items():
        print(f"{entity}: {values}")

    print("\nExtraction completed!")
