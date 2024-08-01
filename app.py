import streamlit as st
import random

# List of cities
cities = [
    "Beijing",
    "Shanghai",
    "Guangzhou",
    "Shenzhen",
    "Chengdu",
    "Chongqing",
    "Tianjin",
    "Xi'an",
    "Hangzhou",
    "Nanjing",
    "Wuhan",
    "Changsha",
    "Qingdao",
    "Dalian",
    "Shenyang",
    "Suzhou",
    "Fuzhou",
    "Jinan",
    "Ningbo",
    "Xiamen",
]

selected_list = []

st.title("City Selector")

# Display checkboxes for city selection
selected_list = st.multiselect("Select cities:", cities, [])

if st.button("Draw a City"):
    if selected_list:
        city = random.choice(selected_list)
        st.write(f"The selected city is: **{city}**")
    else:
        st.write("No cities selected. Please select at least one city.")
