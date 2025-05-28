import os
import io
import requests
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document
import openai
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text(file):
    """Extract text from uploaded resume file based on its type."""
    filename = file.name.lower()
    try:
        if filename.endswith('.pdf'):
            # Extract text from PDF
            text = pdf_extract_text(file)
            return text
        elif filename.endswith('.docx'):
            doc = Document(file)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text
        elif filename.endswith('.txt'):
            return file.getvalue().decode("utf-8")
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        raise RuntimeError(f"Error extracting text from the file: {e}")

def analyze_resume(text):
    """Analyze resume text using OpenAI API for NLP insights."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Extract key skills, experiences, and a professional summary from the following resume content:\n\n{text}",
            temperature=0.5,
            max_tokens=300
        )
        analysis = response.choices[0].text.strip()
        return {"analysis": analysis}
    except Exception as e:
        raise RuntimeError(f"Error during resume analysis: {e}")

def fetch_matching_jobs(keywords):
    """Fetch matching jobs using a public job API."""
    try:
        # For demonstration, using a dummy API endpoint
        endpoint = "https://jobs.github.com/positions.json"  # Replace with a real endpoint if needed
        params = {"description": " ".join(keywords)}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError("Error fetching job listings.")
    except Exception as e:
        raise RuntimeError(f"Error fetching matching jobs: {e}")

def generate_ats_feedback(text):
    """Provide ATS-friendly feedback for the resume."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide detailed ATS-friendly feedback for the following resume content:\n\n{text}",
            temperature=0.5,
            max_tokens=200
        )
        feedback = response.choices[0].text.strip()
        return feedback
    except Exception as e:
        raise RuntimeError(f"Error generating ATS feedback: {e}")
