### Import modules
import streamlit as st
import pandas as pd
import datetime


### Load data difectly from CSV
df = pd.read_csv ('API_SP.DYN.LE00.IN_DS2_en_csv_v2_3731279.csv')

### UI elements
st.title("Welcome")
st.subheader("Input your Data")

# Generate list of countries from csv data
country = df['Country Name']
# Ask for user geo informations
country_birth = st.selectbox("Country of birth", country)
country_residence = st.selectbox("Country of residence", country)
# Ask for birthdate in format Y-m-d, range from 1960-2010 & extract year
date_birth = st.date_input("Enter date of birth",value= datetime.date(2010,1,1),
            min_value = datetime.date(1960,1,1),max_value = datetime.date(2010,1,1))
date_birth = datetime.datetime.strptime(str(date_birth),"%Y-%m-%d")
# Gender information
# Current Data source no gender info
#Gender = st.radio('Enter Gender',['Female','Male','Other'])

### Get value in df
# hardcoded, based on specific source
st.subheader('life expectancy')
country_row_birth = df.loc[df['Country Name'] == str(country_birth)]
country_row_residence = df.loc[df['Country Name'] == str(country_residence)]
year_birth = str(date_birth.year)
life_exp_1 = country_row_birth[year_birth].values[0]
life_exp_2 = country_row_residence[year_birth].values[0]
st.subheader('When you where born you had a life expectancy of : ' + str(life_exp_1) + ' years')
st.subheader('In comparision, life expectancy in your country of residence for the same year was : '\
            + str(life_exp_1) + ' years')

# TODO :    - Get multiple source
#           - Add more analysis ad visualisations (comparision exptancy gaines by moving, 
#               comparision in time, if born today etc)
#           - Keep script seperated if usage in another framework
#           - Check for data limit for hosting, find free host solution as data no sensitive
#           - Deploy as application for test
#           - Write documentation 