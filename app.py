import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import openai


openai.api_key =os.getenv( "YOUR_API_KEY")


# job description template
def generate_job_description(job_title, company_name, brief_description, skills, experience_level):
    prompt_template = """
    Generate a job description for the following role:

    Job Title: {job_title}
    Company: {company_name}
    Brief Job Description: {brief_description}
    Desired Skills: {skills}
    Experience Level: {experience_level}

    Provide a detailed and professional job description.
    """

    prompt = prompt_template.format(
        job_title=job_title,
        company_name=company_name,
        brief_description=brief_description,
        skills=skills,
        experience_level=experience_level
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    return response.choices[0].text.strip()



def app():
    st.title("AI-Powered Job Description Generator")


    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    brief_description = st.text_area("Brief Job Description")
    skills = st.text_input("Desired Skills (comma separated)")
    experience_level = st.selectbox("Experience Level", ["Entry-Level", "Mid-Level", "Senior"])

    if st.button("Generate Job Description"):
        if job_title and company_name and brief_description and skills and experience_level:
            job_description = generate_job_description(job_title, company_name, 
                            brief_description, skills, experience_level)
            
            st.subheader("Generated Job Description")
            st.write(job_description)
        else:
            st.error("Please fill out all fields.")

if __name__ == "__main__":
    app()
 

