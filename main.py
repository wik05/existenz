import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Load data
df = pd.read_csv (r'/Users/rhyzom/Downloads/API_SP.DYN.LE00.IN_DS2_en_csv_v2_3731279.csv')
country = df['Country Name']
st.title("Welcome")
st.subheader("Input your Data")
country_birth = st.selectbox("Country of birth", country)
country_residence = st.selectbox("Country of residence", country)
date_birth = st.date_input("enter date of birth",value= datetime.date(2010,1,1),min_value = datetime.date(1960,1,1),max_value = datetime.date(2010,1,1))

date_birth = datetime.datetime.strptime(str(date_birth),"%Y-%m-%d")



st.subheader('life expectancy')
c_b = df.columns.get_loc('Country Code')
c_r = df.loc[df['Country Name'] == str(c_b)]

rsu = c_r[str(date_birth.year)].values
st.text('Your expectd to live until : ' + str(rsu[0]))
