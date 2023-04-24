import streamlit as st
import pandas as pd
import numpy as np
import os

#Page heading
st.header(":red[Location] of Pubs")

#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "Resources")
DATA_PATH1 = os.path.join(dir_of_interest,"Data", "Pub.csv")
df = pd.read_csv(DATA_PATH1)

#Display Pub Locations by Zip Code, Local Authority
unique=['Post Code', 'Local Authority','Pub Name']

option=st.radio(label="Select Below Option to See the Available Pubs",
                options=unique, horizontal=False)

if option=='Post Code':
    selected=st.selectbox(label='Select the ZipCode',options=df['Post Code'].unique())
    st.subheader(f"Total Pubs Found : {df[df['Post Code']==selected].shape[0]}")
    st.map(data=df[df['Post Code']==selected],  use_container_width=True)
elif option=='Pub Name':
    selected=st.selectbox(label='Select the Pub Name',options=df['Name'].unique())
    st.subheader(f"Total Pubs Found : {df[df['Name']==selected].shape[0]}")
    st.map(data=df[df['Name']==selected],  use_container_width=True)
else :
    selected=st.selectbox(label='Select Local Authority',options=df['Area'].unique())
    st.subheader(f"Total Pubs Found : {df[df['Area']==selected].shape[0]}")
    st.map(data=df[df['Area']==selected],  use_container_width=True)