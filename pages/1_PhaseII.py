import streamlit as st
import pandas as pd
import info


# About Me Section
def about_me_section():
    st.header("About Me")
    #st.image(info.profile_picture, width=200)
    st.write(info.about_me)
    st.write("---")
about_me_section()

# Sidebar Links
def links_section():
    st.sidebar.header("Links")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

    youtube_link = f'<a href="{info.my_youtube_url}"><img src="{info.youtube_image_url}" alt="Youtube" width="75" height="75"></a>'
    st.sidebar.markdown(youtube_link, unsafe_allow_html=True)
links_section()

# User Input Example
name = st.text_input("Enter your name:", "Movie Enthusiast")  # NEW
st.write(f"Welcome, {name}! Let's talk movies.")

# Education Section
def education_section():
    st.header("Education 📚")
    st.subheader(f'**{info.education_data["Institution"]}**')
    st.write(f'**Degree:** {info.education_data["Degree"]}')
    st.write(f'**Graduation Date:** {info.education_data["Graduation Date"]}')
    st.write(f'**GPA:** {info.education_data["GPA"]}')
    st.write("**Relevant Coursework:**")
    st.write("---")
    
    # Convert course_data into a Pandas DataFrame
    coursework = pd.DataFrame(info.course_data)
    
    # Display DataFrame with custom column names
    st.dataframe(
        coursework.rename(columns={
            "code": "Course Code",
            "names": "Course Name",
            "semester_taken": "Semester Taken",
            "skills": "What I Learned"
        }),
        hide_index=True
    )
    st.write("---")
education_section()

# Review Journey Section
def review_journey_section():
    st.header("Review Journey")
    for job_title, (job_description, image) in info.reviewJourney_data.items():
        expander = st.expander(f"{job_title}")
        #expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
review_journey_section()

# Skills Section
def skills_section():
    st.header("Skills")
    st.subheader("Filmmaking")
    for skill, percentage in info.filmmaking_data.items():
        st.write(f"{skill}")
        st.progress(percentage)
    
    st.subheader("Spoken Languages")
    for spoken, proficiency in info.spoken_data.items():
        st.write(f"{spoken}: {proficiency}")
    st.write("---")
skills_section()


# Awards Section
def awards_section():
    st.header("Awards")
    for title, (details, image) in info.awards_data.items():
        expander = st.expander(f"{title}")
        #expander.image(image, width=250)
        for bullet in details:
            expander.write(bullet)
    st.write("---")
awards_section()
