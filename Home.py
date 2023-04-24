import streamlit as st
import os
from matplotlib import image
import pandas as pd

FILE_DIR1 = os.path.dirname(os.path.abspath("__file__"))
dir_of_interest = os.path.join(FILE_DIR1,"Resources","Data","Pub.csv")
pub_img = os.path.join(FILE_DIR1,"Resources","Image","PubIMG.jpg")

st.title('**_Pub Finder in United Kingdom_**')

# Displaying image
img = image.imread(pub_img)
st.image(img)

if st.button('Click to know Details'):
    df = pd.read_csv(dir_of_interest)
    st.dataframe(df)

    st.subheader(f"Total Pubs in UK:- :blue[{df['Name'].nunique()}]")
    
    st.subheader(f"Total Post Codes in UK:- :blue[{df['Post Code'].nunique()}]")
   
    st.subheader(f"Total Local Authorities in UK:- :blue[{df['Area'].nunique()}]")

st.markdown('This is a simple app to find the 5 nearest pubs in United Kingdom from the location given by the user.\n The data was provided by :red[Innomatics] Research Labs')

st.subheader('My Social Handles')
st.markdown("[Github Account](https://github.com/AkshantYadav)")

st.markdown("[LinkedIn Account](https://www.linkedin.com/in/akshantyadav/)")