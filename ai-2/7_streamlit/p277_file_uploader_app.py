import streamlit as st
from io import StringIO

st.title("스트림릿의 파일 업데이트 사용 예")
uploaded_file = st.file_uploader("Text파일을 선택하세요", type="txt")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(string_data[:100])

uploaded_file = st.file_uploader("mp3 파일을 선택하세요." , type="mp3")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data[:100])
