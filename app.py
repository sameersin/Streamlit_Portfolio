import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shaik Sameer"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD ASSETS ---
#img_profile = Image.open("resources/images/profile-pic.png")


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    #st.image(img_profile, width=230)
    st.image("https://avatars.githubusercontent.com/u/76248384?v=4", width=230)

with col2:
    st.title("Shaik Sameer", anchor=False)
    st.write("_Aspiring Data scientist_")
    st.write(
        """
A resilient engineer with expertise in statistical analysis and machine learning.
Proficient in Python, R, SQL, and Tableau.
Skilled in data cleaning, feature engineering, and model evaluation.
Passionate about solving complex problems and eager to contribute to world.
"""
    )
    st.write("📫", "sameershaik78@gmail.com")


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(2)
with cols[0]:
    st.write(':pushpin: [Likedin](https.linkedin.com/in/sameershaik78/)')
with cols[1]:
    st.write(':safety_pin: [Github](https.github.com/sameersin)')
