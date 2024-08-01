import streamlit as st
import random

# Initialize the list of Chinese cities if it doesn't exist in session state
if "cities" not in st.session_state:
    st.session_state.cities = [
        "阿那亚",
        "成都",
        "武汉",
        "青岛",
        "潮汕",
        "顺德",
        "小樽",
        "火奴鲁鲁",
    ]

# Initialize the selected cities dictionary if it doesn't exist in session state
if "selected_cities" not in st.session_state:
    st.session_state.selected_cities = {}

st.title("大志的都市抽样器")

# Custom CSS for button styling
st.markdown(
    """
<style>
    .stButton>button {
        width: 100%;
        font-weight: bold;
    }
    .decrease {
        background-color: #ff4b4b;
        color: white;
    }
    .increase {
        background-color: #4CAF50;
        color: white;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Input for adding new cities
new_city = st.text_input("加入新城市:")
if st.button("阁下有请"):
    if new_city and new_city not in st.session_state.cities:
        st.session_state.cities.append(new_city)
        st.success(f"Added {new_city} to the list!")
    elif new_city in st.session_state.cities:
        st.warning(f"{new_city} is already in the list!")
    else:
        st.warning("Please enter a city name!")

# Display cities and allow multiple selections
st.subheader("挑吧:")

# Create three columns for better layout
col1, col2, col3 = st.columns(3)

for i, city in enumerate(st.session_state.cities):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        city_count = st.session_state.selected_cities.get(city, 0)

        st.write(f"**{city}**")
        col_left, col_right = st.columns([1, 1])
        with col_left:
            if st.button(
                "➖",
                key=f"remove_{city}",
                disabled=city_count == 0,
                help="Decrease count",
            ):
                st.session_state.selected_cities[city] = max(0, city_count - 1)
        with col_right:
            if st.button("➕", key=f"add_{city}", help="Increase count"):
                st.session_state.selected_cities[city] = city_count + 1

        st.write(f"选取次数: {city_count}")
        st.write("---")

# Display selected cities with counts
st.subheader("都在这里:")
selected_cities = [
    city
    for city, count in st.session_state.selected_cities.items()
    for _ in range(count)
]
for city, count in st.session_state.selected_cities.items():
    if count > 0:
        st.write(f"{city}: {count}")

# Generate random sample
sample_size = st.number_input("想选几个苹果", min_value=1, value=1)
if st.button("随机吧！"):
    if selected_cities:
        sample = random.choices(selected_cities, k=sample_size)
        st.success(f"出发去: {', '.join(sample)}")
    else:
        st.warning("Please select at least one city before generating a sample!")
