import streamlit as st


st.image(
    "https://images.unsplash.com/photo-1720598982902-cb1210b60872?q=80&w=3941&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    use_column_width=True,
)
st.markdown("# 大志's gadgets :sparkles:")
st.divider()
# st.sidebar.markdown("# Main page 🎈")

# pg = st.navigation([st.Page("1_randcity.py"), st.Page("test.py")])

rand_city_pg = st.Page("1_randcity.py", title="随机城市", icon="✈️")
page2 = st.Page("2_map.py", title="待测试", icon="🚀")
pg = st.navigation([rand_city_pg, page2])
pg.run()
