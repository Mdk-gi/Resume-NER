from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "google-bert/bert-base-cased"

print("Downloading BERT tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Downloading BERT model...")

model = AutoModelForTokenClassification.from_pretrained(
    model_name,
    num_labels=9
)

print("BERT downloaded successfully!")
