import streamlit as st
st.title("스트림릿의 샐렉트 박스 사용 예")

selectbox1_options = ['하이톤','모차르츠','벤토벤','슈만']
your_option1 = st.selectbox('좋아하는 음악가는?', selectbox1_options)
st.write('**당신의 선택** :', your_option1)

selectbox2_options = ['보티첼리','햄브리드','피카소','뭉크']
your_option2 = st.selectbox('좋아하는 음악가는?', selectbox2_options)
st.write('**당신의 선택** :', your_option2)