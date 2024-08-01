import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.colors as mcolors


cities_data = [
    {"city": "北京", "latitude": 39.9042, "longitude": 116.4074},
    {"city": "上海", "latitude": 31.2304, "longitude": 121.4737},
    {"city": "广州", "latitude": 23.1291, "longitude": 113.2644},
    {"city": "深圳", "latitude": 22.5431, "longitude": 114.0579},
    {"city": "成都", "latitude": 30.5728, "longitude": 104.0668},
    {"city": "重庆", "latitude": 29.5630, "longitude": 106.5516},
    {"city": "天津", "latitude": 39.3434, "longitude": 117.3616},
    {"city": "西安", "latitude": 34.3416, "longitude": 108.9398},
    {"city": "杭州", "latitude": 30.2741, "longitude": 120.1551},
    {"city": "南京", "latitude": 32.0603, "longitude": 118.7969},
    {"city": "武汉", "latitude": 30.5928, "longitude": 114.3055},
    {"city": "长沙", "latitude": 28.2282, "longitude": 112.9388},
    {"city": "青岛", "latitude": 36.0662, "longitude": 120.3826},
    {"city": "大连", "latitude": 38.9140, "longitude": 121.6147},
    {"city": "沈阳", "latitude": 41.8057, "longitude": 123.4328},
    {"city": "苏州", "latitude": 31.2989, "longitude": 120.5853},
    {"city": "福州", "latitude": 26.0745, "longitude": 119.2965},
    {"city": "济南", "latitude": 36.6512, "longitude": 117.1201},
    {"city": "宁波", "latitude": 29.8683, "longitude": 121.5440},
    {"city": "厦门", "latitude": 24.4798, "longitude": 118.0895},
]

# Create DataFrame
df = pd.DataFrame(cities_data)
colors = sns.color_palette("hls", n_colors=len(df))
colors_hex = np.array([mcolors.rgb2hex(color) for color in colors])
df["color"] = colors_hex
st.map(df, color="color")
