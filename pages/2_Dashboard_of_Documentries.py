import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "documentary.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "documentriesfinal5.csv")
st.title("Dashboard of Documentaries")
img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
#st.dataframe(df)

#documentary = st.selectbox("Select the Distributor:", df["Distributor"].head(10))
if st.button('View full data'):
     st.dataframe(df)    
else:
    pass
documentary = st.selectbox("Select the Distributor:", df["Distributor"].head(10))
st.dataframe(df[df['Distributor']==documentary].sort_values(['Lifetime_Gross'],ascending=False))


#st.dataframe(df[df['Distributor']==documentary].sort_values(['Lifetime_Gross'],ascending=False))

I1 = os.path.join(dir_of_interest, "images", "Release year Vs Lifetime Gross.jpg")
I2 = os.path.join(dir_of_interest, "images", "Top 20 Distributors by Collections.jpg")
I5 = os.path.join(dir_of_interest, "images", "Year wise Distributor's Releases.jpg")
I4 = os.path.join(dir_of_interest, "images", "Year Wise Opening and Lifetime Collections.jpg")
I3 = os.path.join(dir_of_interest, "images", "Top 20 Distributors by Titles.jpg")

img1 = st.selectbox("select data to analyse:", ("Release year Vs Lifetime Gross", "Top 20 Distributors by Collections ", "Top 20 Distributors by Titles ", "Year Wise Opening and Lifetime Collections ","Year wise Distributor's Releases "))

st.write('You selected:', img1)

img2 = False

if img1 == "Release year Vs Lifetime Gross":
    img2 = I1
elif img1 == "Top 20 Distributors by Collections ":
    img2 = I2
elif img1 == "Top 20 Distributors by Titles ":
    img2 = I3
elif img1 == "Year Wise Opening and Lifetime Collections ":
    img2 = I4
else:
    img2 = I5

if img2!=False:
    img = image.imread(img2)
    st.image(img2)





