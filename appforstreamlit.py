import os
os.system("cls")
import pandas as pd
import numpy as np
import streamlit as st

st.sidebar.markdown("👤 Developed by B Vivekananda Raju")
st.title('Uber Pickups in NYC')

DATE_COLUMN='date/time'
DATA_URL=('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase=lambda x:str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text('Loading data....')
data=load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader("No Of pickups in an Hour")
hist_values=np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

st.subheader('Map of all Pickups')
st.map(data)

hour_to_filter=st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of pickups at {hour_to_filter}:00')
st.map(filtered_data)
