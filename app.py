import streamlit as st

# 页面只显示 我爱你
st.title("❤️ 我爱你 ❤️")

# 输入框
text = st.text_input("输入任意内容")

# 只要输入任何东西，就弹窗 刘慧婷我爱你
if text:
    st.success("刘慧婷我爱你")