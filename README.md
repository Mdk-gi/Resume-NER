# Resume NER – AI-Powered Resume Information Extractor

An AI-powered Resume Information Extraction system that uses a fine-tuned BERT model and a Gemini AI Agent to extract, review, and organize candidate information from PDF resumes.

## Live Demo

**Live Application:** https://mdk-resume-ner.streamlit.app/

**GitHub Repository:** https://github.com/Mdk-gi/Resume-NER

## Project Overview

Resume NER is an AI-based application designed to simplify the process of extracting structured information from resumes.

The system uses a fine-tuned BERT model for Named Entity Recognition (NER) to identify important information from resume text. A Gemini AI Agent then reviews and organizes the extracted information into a structured candidate profile.

Users can upload a resume PDF and optional supporting documents through a Streamlit interface.

## Key Features

- Upload resumes in PDF format.
- Extract candidate information using a fine-tuned BERT model.
- Identify 12 different entity categories.
- Use a Gemini AI Agent to review and organize extracted information.
- Upload optional supporting PDF documents.
- Generate structured candidate profiles.
- Identify missing information.
- Download extracted information in JSON format.
- Simple and interactive Streamlit interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| BERT | Named Entity Recognition |
| PyTorch | Model execution |
| Transformers | BERT model and tokenizer |
| Gemini API | AI-powered information review and organization |
| Streamlit | Web application interface |
| PyMuPDF | PDF text extraction |
| Git & GitHub | Version control and project hosting |

## System Architecture

The project follows this workflow:

1. **Resume Upload:** User uploads a resume PDF through the Streamlit application.
2. **Text Extraction:** PyMuPDF extracts text from the uploaded PDF.
3. **BERT Model:** The fine-tuned BERT model identifies entities from the extracted text.
4. **Gemini AI Agent:** The extracted information is reviewed and organized into a structured profile.
5. **Final Output:** The application displays candidate information, missing fields, and provides a JSON download option.

## Entity Categories

The fine-tuned BERT model identifies the following 12 entity categories:

| Entity | Description |
|---|---|
| NAME | Candidate name |
| EMAIL | Email address |
| PHONE | Phone number |
| SKILL | Technical and professional skills |
| DEGREE | Educational qualification |
| COLLEGE | College or university |
| COMPANY | Company name |
| DESIGNATION | Job designation |
| EXPERIENCE | Work experience |
| LOCATION | Candidate location |
| GRADUATION_YEAR | Graduation year |
| CERTIFICATION | Professional certifications |

## Project Structure

```text
Resume-NER/
│
├── agent/
│   └── llm_agent.py
│
├── samples/
│   └── .gitkeep
│
├── src/
│   ├── __init__.py
│   ├── download_model.py
│   ├── evaluation.py
│   ├── extraction.py
│   ├── ocr.py
│   ├── predict.py
│   ├── preprocessing.py
│
├── .env.example
├── .gitignore
├── MODEL_CARD.md
├── README.md
├── app.py
├── requirements.txt
└── train_ner.py
```

## Model Information

- **Model:** Fine-Tuned BERT
- **Base Model:** google-bert/bert-base-cased
- **Architecture:** BERT Token Classification
- **Task:** Named Entity Recognition
- **Framework:** PyTorch
- **Entity Categories:** 12

The pretrained BERT model was fine-tuned using an annotated resume NER dataset prepared for this project.

The trained model is stored separately from the GitHub source code and downloaded from the project's GitHub Release when required.

**Model Release:** https://github.com/Mdk-gi/Resume-NER/releases/tag/version

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Mdk-gi/Resume-NER.git
cd Resume-NER
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a `.env` file in the project root directory.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your actual API key to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Deployment

The application is deployed using Streamlit Community Cloud.

- **Frontend:** Streamlit
- **Source Code:** GitHub
- **Trained Model:** GitHub Release
- **AI Agent:** Gemini API

The trained BERT model is downloaded automatically from the GitHub Release when it is not available locally.

## Limitations

- Extraction accuracy depends on resume formatting and text quality.
- Unusual layouts may affect entity recognition.
- Some information may be missed or incorrectly classified.
- Extracted information should be reviewed before professional use.
- Gemini AI Agent output may require verification.

## Future Improvements

- Improve entity recognition accuracy.
- Expand the training dataset.
- Support additional resume formats.
- Improve extraction for complex resume layouts.
- Add more evaluation and validation capabilities.

## Author

**Mohammed Jalil Kurupkar**

B.Tech – Computer Science and Engineering  
Specialization: AI and Analytics

GitHub: https://github.com/Mdk-gi

## License

This project is developed for educational and academic purposes.
