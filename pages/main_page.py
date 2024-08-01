import streamlit as st


st.image("./static/xinjiang.jpg", use_column_width=True)
st.markdown("# 大志's gadgets :sparkles:")
st.divider()
# st.sidebar.markdown("# Main page 🎈")

# pg = st.navigation([st.Page("1_randcity.py"), st.Page("test.py")])

rand_city_pg = st.Page("1_randcity.py", title="随机城市", icon="✈️")
page2 = st.Page("2_map.py", title="待测试", icon="🚀")
pg = st.navigation([rand_city_pg, page2])
pg.run()
