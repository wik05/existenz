### Import modules
import streamlit as st
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta



### Load data difectly from CSV
df = pd.read_csv ('API_SP.DYN.LE00.IN_DS2_en_csv_v2_3731279.csv')

### UI elements
st.title("Welcome to Existenz")
st.write('This website provides a simple tool to roughly calculate your life expectency from know' + 
        'The aime is have have a batter awareness of the time of our existence.')
st.subheader("Enter some data about you for the computation")

# Generate list of countries from csv data
country = df['Country Name']
# Ask for user geo informations
country_birth = st.selectbox("Country of birth", country)
country_residence = st.selectbox("Country of residence", country)
# Ask for birthdate in format Y-m-d, range from 1960-2010 & extract year
date_birth = st.date_input("Enter date of birth in format YYYY-D-M",value= datetime.date(2010,1,1),
            min_value = datetime.date(1960,1,1),max_value = datetime.date(2010,1,1))
date_birth = datetime.datetime.strptime(str(date_birth),"%Y-%m-%d")
now = datetime.datetime.now()
# Gender information
# Current Data source no gender info
#Gender = st.radio('Enter Gender',['Female','Male','Other'])

### Get value in df
# hardcoded, based on specific source
st.header('Life Expectancy')
country_row_birth = df.loc[df['Country Name'] == str(country_birth)]
country_row_residence = df.loc[df['Country Name'] == str(country_residence)]
year_birth = str(date_birth.year)
life_exp_1 = country_row_birth[year_birth].values[0]
life_exp_2 = country_row_residence[year_birth].values[0]

st.subheader('Expererienced')
age1,age2,age3 = st.columns(3)
age1.metric('Time of existence in Years',now.year-date_birth.year)
age2.metric('Time of existence in Days',(now.year-date_birth.year)*365)
age3.metric('Time of existence in Hours',(now.year-date_birth.year)*8760)
#rdelta = relativedelta(now.year, date_birth.year)
#st.metric('comp',rdelta.years)

st.subheader('Expected time to experience')
bir1,bir2,bir3 = st.columns(3)
bir1.metric('Time of existence in Years',round(life_exp_1))
bir2.metric('Time of existence in Days',round(life_exp_1*365))
bir3.metric('Time of existence in Hours',round(life_exp_1*8760))

res1,res2,res3 = st.columns(3)
res1.metric('Time of existence in Years',round(life_exp_2))
res2.metric('Time of existence in Days',round(life_exp_2*365))
res3.metric('Time of existence in Hours',round(life_exp_2*8760))


# TODO :    - Get multiple source
#           - Add more analysis ad visualisations (comparision exptancy gaines by moving, 
#               comparision in time, if born today etc)
#           - Keep script seperated if usage in another framework
#           - Check for data limit for hosting, find free host solution as data no sensitive
#           - Deploy as application for test
#           - Write documentation 
#           - Compute age and substract from complete time
#           - Convert time to Days, hours, time seconds etc.