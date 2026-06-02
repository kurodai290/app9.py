import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Corporate Wars Premium", layout="wide")

# 同じフォルダにあるHTMLファイルを読み込むだけ（html_codeの記述は完全に廃止）
html_path = os.path.join(os.path.dirname(__file__), "app9.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=850, scrolling=True)
