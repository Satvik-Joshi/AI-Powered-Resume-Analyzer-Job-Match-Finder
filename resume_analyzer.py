# resume_analyzer.py

import re
from collections import Counter

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

def extract_keywords(text):
    words = clean_text(text).split()
    return Counter(words)

def calculate_match_score(resume_text, job_text):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    common = sum((resume_keywords & job_keywords).values())
    total = sum(job_keywords.values())

    score = round((common / total) * 100, 2) if total > 0 else 0
    missing = list(set(job_keywords) - set(resume_keywords))

    return score, missing
