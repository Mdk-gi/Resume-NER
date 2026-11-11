# Model Card – Resume NER

## Model Overview
This project uses a fine-tuned BERT model for Named Entity Recognition (NER) to extract structured information from resumes.

## Model Details
- **Model Name:** Resume NER – Fine-Tuned BERT
- **Base Model:** google-bert/bert-base-cased
- **Model Architecture:** BERT Token Classification
- **Task:** Named Entity Recognition (NER)
- **Framework:** PyTorch and Transformers

## Intended Use
The model is designed to identify and extract candidate information from resume text, including personal details, education, skills, and work experience.

## Entity Labels
The model identifies 12 entity categories:

1. NAME
2. EMAIL
3. PHONE
4. SKILL
5. DEGREE
6. COLLEGE
7. COMPANY
8. DESIGNATION
9. EXPERIENCE
10. LOCATION
11. GRADUATION_YEAR
12. CERTIFICATION

## Training Information
The pretrained BERT model was fine-tuned using an annotated resume NER dataset prepared for this project.

## Limitations
- Extraction accuracy depends on resume formatting and text quality.
- Unusual layouts and scanned documents may affect extraction.
- Some entities may be missed or incorrectly classified.
- Results should be reviewed before professional use.

## Application Integration
The trained model is integrated into a Streamlit application. A Gemini AI Agent reviews and organizes the extracted information into a structured candidate profile.

## Disclaimer
This model is developed for educational and project purposes. Extracted information should be verified by users.
