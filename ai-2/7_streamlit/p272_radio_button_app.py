import streamlit as st
import dandas as pd

st.title("스트림릿의 라이도 박스 사용 예")

radio1_optiones = {'10','20','30','40'}
radio1_selected = st.radio('(5x5+5)의 값은 얼마일까요?', radio1_optiones)
st.write('**선택한 답** :', radio1_selected)

radio2_options = ['마라톤','축구','수영','승마']
radio2_selected = st.radio('당신이 좋아하는 운동은?',radio2_options,index=2,horizontal=True)
st.write('**당신의 선택은** :', radio2_selected)