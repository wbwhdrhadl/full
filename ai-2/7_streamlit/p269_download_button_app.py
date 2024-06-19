import streamlit as st
import pandas as pd
from io import BytestID

st.title("스트림릿의 다운로드 버튼 사용 예")

st.subheader("텍스트 파일 다운로드 예제")

folder = "./data/"

with open(folder + '서연의_이야기.txt', encoding='utf-8') as text_file:
    text_data = text_file.read()
    st.download_button(
        label="텍스트 파일 다운로드",
        data= text_data,
        file_name='서연의_이야기.txt',

    )

st.subheader("이미지 파일 다운로드 예제")

with open(folder + 'sanole_image.png','rb') as img_file:
    st.download_button(
        label='이미지 파일 다운로드',
        data = img_file,
        file_name='sample_image.png',
        mimr= 'image/png'
    )
st.subheader("오디오 파일 다운로드 예제")

with open(folder + 'saple.csv', 'rb') as csv_file:
    st.download_button(
        label='오디오 파일 다운로드',
        data = csv_file,
        file_name = '서연의_하루_TTS_배경음악_short.mp3',
        mime='audio.mpeg'
    )