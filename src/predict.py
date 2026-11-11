
from pathlib import Path
import torch
import urllib.request
import zipfile

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

MODEL_URL = (
    "https://github.com/Mdk-gi/Resume-NER/releases/download/"
    "version/p30_bert_final.zip"
)

# =====================================
# 2. DEVICE
# =====================================

device = 0 if torch.cuda.is_available() else -1

print("Loading trained resume NER model...")
print("Device:", "GPU" if device == 0 else "CPU")

# =====================================
# 3. DOWNLOAD MODEL IF MISSING
# =====================================

model_file = LOCAL_MODEL_PATH / "model.safetensors"

if not model_file.exists():

    print("Trained model not found locally.")
    print("Downloading trained model from GitHub Release...")

    LOCAL_MODEL_PATH.mkdir(parents=True, exist_ok=True)

    zip_path = PROJECT_ROOT / "p30_bert_final.zip"

    try:

        urllib.request.urlretrieve(
            MODEL_URL,
            zip_path
        )

        print("Model downloaded successfully!")

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(LOCAL_MODEL_PATH)

        print("Model extracted successfully!")

    finally:

        if zip_path.exists():
            zip_path.unlink()

# =====================================
# 4. VERIFY MODEL FILES
# =====================================

required_files = [
    "config.json",
    "model.safetensors",
    "tokenizer.json",
    "tokenizer_config.json"
]

missing_files = [
    name
    for name in required_files
    if not (LOCAL_MODEL_PATH / name).exists()
]

if missing_files:
    raise FileNotFoundError(
        f"Missing trained model files: {missing_files}"
    )

# =====================================
# 5. LOAD TRAINED BERT MODEL
# =====================================

print("Loading trained BERT tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    str(LOCAL_MODEL_PATH),
    local_files_only=True
)

print("Loading trained BERT model...")

model = AutoModelForTokenClassification.from_pretrained(
    str(LOCAL_MODEL_PATH),
    local_files_only=True
)

print("Trained model loaded successfully!")

# =====================================
# 6. CREATE PIPELINE
# =====================================

ner_pipeline = pipeline(
    task="token-classification",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple",
    device=device
)

# =====================================
# 7. ENTITY LABELS
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
# 8. ENTITY EXTRACTION
# =====================================

def extract_entities(text):

    if not isinstance(text, str) or not text.strip():
        return {}

    predictions = ner_pipeline(text)

    results = {
        label: [] for label in ENTITY_LABELS
    }

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
# 9. TEST
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
    