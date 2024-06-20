import my_yt_tran
import my_text_sum
import streamlit as st
import openai
import os
import tiktoken
import textwrap
import deepl
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def calc_token_num(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    encoded_list = enc.encode(text)
    token_num = len(encoded_list)

    return token_num


def divide_text(text, token_num):
    req_max_token = 2000

    divide_num = int(token_num / req_max_token) + 1
    divide_char_num = int(len(text) / divide_num)
    divide_width = divide_char_num + 20

    divide_text_list = textwrap.wrap(text, width=divide_width)

    return divide_num,divide_text_list


def summarize_youtube_video(video_url, selected_lang, trans_method):
    if selected_lang == "영어":
        lang = "en"
    else:
        lang = "ko"

    st.video(video_url, format="video/mp4")

    _, yt_title, _, _, yt_duration = my_yt_tran.get_youtube_video_info(video_url)
    st.write(f"[제목] {yt_title}, [길이(분:초] ({yt_duration})")

    try:
        yt_transcript = my_yt_tran.get_transcript_from_youtube(video_url, lang=lang)
    except NoTranscriptFound:
        st.error("자막을 찾을 수 없습니다. 다른 동영상을 시도해주세요.")
        return
    except TranscriptsDisabled:
        st.error("이 동영상의 자막이 비활성화되어 있습니다.")
        return
    except Exception as e:
        st.error(f"자막을 가져오는 중 오류가 발생했습니다. {str(e)}")
        return
    
    token_num = calc_token_num(yt_transcript)

    div_num, divided_yt_transcript = divide_text(yt_transcript, token_num)

    st.write("유튜브 동영상 내용 요약 중입니다. 잠시만 기다려 주세요.")

    summaries = []

    for divide_text in divided_yt_transcript:
        summary = my_text_sum.summarize_text(divide_text, lang=lang)
        summaries.append(summary)

    _, final_summary = my_text_sum.summarize_text_final(summaries, lang=lang)

    if selected_lang == "영어":
        shorten_num = 200
    else:
        shorten_num = 120

    shorten_final_summary = textwrap.shorten(final_summary, shorten_num, placeholder=" [...이하 생략...]")
    st.write("- 최종 요약(축약): ", shorten_final_summary)

    if selected_lang == "영어":
        if trans_method == "OpenAI":
            trans_result = my_yt_tran.translate_english_to_korean_using_openAI(final_summary)
        elif trans_method == "DeepL":
            trans_result = my_yt_tran.translate_english_to_korean_using_deepL(final_summary)

        shorten_trans_result = textwrap.shorten(trans_result, shorten_num, placeholder=" [...이하 생략...]")
        st.write("- 한국어 요약(번역): ", shorten_trans_result)



# ------------------- 콜백 함수 --------------------
def button_callback():
    st.session_state['input'] = ""

# ------------- 사이드바 화면 구성 --------------------------   
st.sidebar.title('요약 설정')
url_text = st.sidebar.text_input('유튜브 동영상의 URL을 입력하세요.', key="input")

clicked_for_clear = st.sidebar.button('URL 입력 내용 지우기', on_click=button_callback)

yt_lang = st.sidebar.radio('유튜브 동영상 언어 선택', ['한국어', '영어'], index=0, horizontal=True)

if yt_lang == '영어':
    trans_method = st.sidebar.radio('번역 방법 선택', ['OpenAI', 'DeepL'], index=1, horizontal=True)
else:
    trans_method = ""

clicked_for_sum = st.sidebar.button('동영상 내용 요약')

# ------------- 메인 화면 구성 --------------------------   
st.title("유튜브 동영상 요약")

if url_text and clicked_for_sum:
    yt_video_url = url_text.strip()

    summarize_youtube_video(yt_video_url, yt_lang, trans_method)
    