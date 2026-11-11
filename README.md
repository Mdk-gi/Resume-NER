# Resume Profile Extractor

An AI-powered Resume Profile Extractor that uses a Fine-Tuned BERT model and a Gemini AI Agent to extract, analyze, review, and organize candidate information from resumes and supporting documents.

## Live Demo

**Live Application:** https://mdk-resume-ner.streamlit.app/

**GitHub Repository:** https://github.com/Mdk-gi/Resume-NER

## Project Overview

The Resume Profile Extractor automates the process of extracting and organizing candidate information from PDF resumes.

The project combines a custom fine-tuned BERT Named Entity Recognition (NER) model with a Gemini-powered AI Agent to produce structured candidate profiles.

Users can upload a resume along with optional supporting documents such as certificates, marksheets, and experience letters.

## Key Features

- Upload PDF resumes.
- Upload multiple supporting PDF documents.
- Extract candidate information using a fine-tuned BERT model.
- Review and organize extracted information using a Gemini AI Agent.
- Identify missing candidate information.
- Generate structured candidate profiles.
- Download the final candidate profile in JSON format.
- Simple and user-friendly Streamlit interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| BERT | Named Entity Recognition |
| PyTorch | Deep learning framework |
| Hugging Face Transformers | BERT model and tokenizer |
| Gemini API | AI-powered information review |
| Streamlit | Web application interface |
| PyMuPDF | PDF text extraction |
| Git & GitHub | Version control and source code hosting |

## System Architecture

1. **Resume Upload:** Users upload a resume and optional supporting documents.
2. **PDF Processing:** PyMuPDF extracts text from the uploaded PDF files.
3. **BERT Extraction:** The fine-tuned BERT model identifies candidate entities.
4. **AI Agent Review:** The Gemini AI Agent reviews and organizes the extracted information using resume context and supporting documents.
5. **Profile Generation:** The application prepares a structured candidate profile and identifies missing information.
6. **Download:** Users can download the final profile as a JSON file.

## Information Extracted

The application works with 12 entity categories:

- NAME
- EMAIL
- PHONE
- SKILL
- DEGREE
- COLLEGE
- COMPANY
- DESIGNATION
- EXPERIENCE
- LOCATION
- GRADUATION_YEAR
- CERTIFICATION

## Project Structure

```text
Resume-NER/
│
├── agent/
│   └── llm_agent.py
│
├── src/
│   ├── predict.py
│   ├── extraction.py
│   ├── preprocessing.py
│   ├── evaluation.py
│   ├── ocr.py
│   └── download_model.py
│
├── samples/
│
├── app.py
├── train_ner.py
├── test_model.py
├── requirements.txt
├── MODEL_CARD.md
├── README.md
└── .gitignore
```

## Installation and Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mdk-gi/Resume-NER.git
cd Resume-NER
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your actual API key to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

## Deployment

The application is deployed using Streamlit Community Cloud and connected to the GitHub repository.

The trained BERT model is distributed separately through GitHub Releases and downloaded by the application when required.

## Important Notes

- The application currently supports text-based PDF extraction.
- Scanned PDFs requiring OCR are not supported by the current upload workflow.
- Candidate information should be reviewed before making recruitment decisions.
- The Gemini API requires a valid API key.

## Future Improvements

- Improve NER extraction accuracy.
- Enhance entity validation and formatting.
- Integrate OCR for scanned resumes.
- Add advanced candidate search and filtering.
- Improve resume evaluation and reporting.

## Author

**Mohammed Jalil Kurupkar**

B.Tech – Computer Science Engineering (AI & Analytics)

## License

This project is available for educational and demonstration purposes.
