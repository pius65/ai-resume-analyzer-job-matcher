
Built by https://www.blackbox.ai

---

# AI Resume Analyzer + Job Matcher

## Project Overview

The **AI Resume Analyzer + Job Matcher** is a powerful application designed to help job seekers enhance their resumes and find matching job opportunities using artificial intelligence. The app allows users to upload their resumes in various formats (PDF, DOCX, TXT) and provides insights such as key skills, experiences, and ATS-friendly feedback generated using OpenAI's GPT-3 model. Additionally, the application can fetch job listings based on the extracted keywords from the resumes, thus aiding users in their job search.

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Set Up a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required Python packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root of your project and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key
   ```

5. **Run the Application**
   Use Streamlit to run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the application in a web browser (typically, the app will be available at `http://localhost:8501`).
2. **Upload Your Resume**: Click on the file uploader and choose a resume file in PDF, DOCX, or TXT format.
3. **Analyze Resume**: Click the "Analyze Resume" button to get an analysis of your resume including key skills and experiences.
4. **Find Matching Jobs**: Click the "Find Matching Jobs" button to retrieve job listings that match the keywords identified from your resume.
5. **Get ATS Feedback**: Expand the ATS-friendly feedback section and click the corresponding button to receive feedback on how well your resume is tailored for Applicant Tracking Systems (ATS).

## Features

- Upload resumes in multiple formats (PDF, DOCX, TXT).
- Extract and display text from uploaded resumes.
- Analyze resumes using OpenAI's GPT-3 for insights on skills and experiences.
- Fetch job listings based on keywords extracted from resumes.
- Provide ATS-friendly feedback to improve the structure and content of resumes.

## Dependencies

The project requires the following Python packages, as outlined in the `requirements.txt` file:

- `streamlit`
- `requests`
- `dotenv`
- `openai`
- `pdfminer.six`
- `python-docx`

Make sure these packages are installed when setting up the project.

## Project Structure

```
ai-resume-analyzer/
│
├── app.py                # Main application file with Streamlit
├── utils.py              # Utility functions for resume text extraction and job fetching
├── betika_live_games.json # Sample data file (not directly used in the application)
├── requirements.txt      # List of dependencies for the project
└── .env                  # Environment variables (not included in version control)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

For any issues or feature requests, please open an issue or a pull request in the repository.