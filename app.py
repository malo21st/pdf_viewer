import streamlit as st

st.config.set_option('public_folder', 'static')
st.config.set_option('public_filetypes', 'pdf')
st.markdown('<a href="https://drive.google.com/file/d/1p69mAARqhB7HratNZgZizPJhcc7aAXOt/view?usp=sharing" target="_blank">PDFを表示</a>', unsafe_allow_html=True)
st.markdown('<a href="/app/static/NOBDATA_ChatGPT活用個別サービス開発資料.pdf" target="_blank">PDFを表示</a>', unsafe_allow_html=True)
st.markdown(
    '<img src="./app/static/tenjikai.png" height="333" style="border: 5px solid orange">',
    unsafe_allow_html=True,
)
st.markdown('<a href="./app/static/tenjikai.png" target="_blank">PDFを表示</a>', unsafe_allow_html=True)
