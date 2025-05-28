import streamlit as st
from utils import extract_text, analyze_resume, fetch_matching_jobs, generate_ats_feedback

st.set_page_config(
    page_title="AI Resume Analyzer + Job Matcher",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header Section with an attractive image from Pexels
st.image("https://images.pexels.com/photos/3182785/pexels-photo-3182785.jpeg", use_container_width=True)
st.title("AI Resume Analyzer + Job Matcher")

st.sidebar.header("Options")

st.header("Upload Your Resume")
uploaded_file = st.file_uploader("Choose a file (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])

if uploaded_file:
    try:
        resume_text = extract_text(uploaded_file)
        st.subheader("Extracted Resume Text")
        st.text_area("", resume_text, height=200)

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing your resume..."):
                analysis_results = analyze_resume(resume_text)
            st.subheader("Resume Analysis")
            st.write(analysis_results.get("analysis", "No analysis available."))

        if st.button("Find Matching Jobs"):
            keywords = ["Python", "NLP", "Machine Learning"]
            with st.spinner("Fetching matching jobs..."):
                jobs = fetch_matching_jobs(keywords)
            if jobs:
                st.subheader("Matching Jobs")
                for job in jobs:
                    st.markdown(f"**{job.get('title', 'No Title')}** at {job.get('company', 'Unknown')}")
                    st.markdown(f"Location: {job.get('location', 'Unknown')}")
                    st.markdown(f"[Apply Here]({job.get('url', '#')})")
                    st.markdown("---")
            else:
                st.error("No matching jobs found or an error occurred while fetching jobs.")

        with st.expander("Show ATS-Friendly Feedback"):
            if st.button("Get ATS Feedback"):
                with st.spinner("Generating feedback..."):
                    feedback = generate_ats_feedback(resume_text)
                st.write(feedback)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload your resume to begin analysis.")
