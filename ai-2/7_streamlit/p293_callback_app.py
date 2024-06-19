import streamlit as st

st.title('콜백 함수 사용 예')

if 'lang' not in st.session_state:
    st.session_state['lang']='영어'

def button_callback(self_lang):
    st.session_state['lang']=self_lang

radio_options = ['영어','프랑스어','독일어']
radio_selected = st.radio('한국어를 어떤 언어로 번역하시겠습니까?', options= radio_options)

clicked = st.button('선택', on_click=button_callback, args=[radio_selected])

st.write(f'한국어를 {st.session_state["lang"]}로 변역하는 것을 선택했습니다.')
