import streamlit as st

st.config.set_option('public_folder', 'static')
st.config.set_option('public_filetypes', 'pdf')
st.markdown('<a href="./static/NOBDATA_ChatGPT活用個別サービス開発資料.pdf" target="_blank">PDFを表示</a>', unsafe_allow_html=True)
st.markdown('<a href="/static/NOBDATA_ChatGPT活用個別サービス開発資料.pdf" target="_blank">PDFを表示</a>', unsafe_allow_html=True)
