
from src.predict import extract_entities

sample_resume = """
AARAV SHARMA
Software Engineer

Email: aarav.sharma.demo@example.com
Phone: +91 98765 43210
Location: Pune, Maharashtra, India

PROFESSIONAL SUMMARY
Software Engineer with 3 years of experience in Python development,
Machine Learning and REST API development.

WORK EXPERIENCE
Software Engineer
BluePeak Technologies
July 2023 - Present

Junior Python Developer Intern
Northstar Digital Labs
January 2023 - June 2023

EDUCATION
Bachelor of Technology (B.Tech) in Computer Science and Engineering
Western Institute of Technology
Graduation Year: 2022

SKILLS
Python, Java, SQL, Machine Learning, Natural Language Processing,
TensorFlow, Scikit-learn, Flask, Django, REST APIs, Git, MySQL, Docker

CERTIFICATIONS
Machine Learning Specialization - DeepLearning.AI
Python for Data Science - IBM SkillsBuild
"""

print("Testing Fine-Tuned BERT Resume NER Model...\n")

results = extract_entities(sample_resume)

entity_names = [
    "NAME", "EMAIL", "PHONE", "SKILL",
    "DEGREE", "COLLEGE", "COMPANY",
    "DESIGNATION", "EXPERIENCE",
    "LOCATION", "GRADUATION_YEAR",
    "CERTIFICATION"
]

for entity in entity_names:
    values = results.get(entity, [])
    print(f"{entity}: {', '.join(values) if values else 'Not Found'}")
