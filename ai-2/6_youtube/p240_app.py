import requests
import os
import textwrap

def summarize_content(contents_url, target_language):
    KAGI_API_KEY = os.environ["KAGI_API_KEY"]

    api_url="https://kagi.com/api/v0/summarize"
    headers = {"Authorization":"Bot " + KAGI_API_KEY}
    parameters = {"url":contents_url, "target_language": target_language}

    r = requests.get(api_url, headers=headers, params=parameters)

    summary = r.json()['data']['output']
    return summary

contents_url = "https://www.youtube.com/watch?v=Ks-_Mh1QhMc"
target_language = "KO"

try:
    summary = summarize_content(contents_url, target_language)
    print(contents_url)
    print(textwrap.shorten(summary, width=150, placeholder=' [...이하 생략...]'))

except:
    print("해당 url의 내용을 요약하지 못했습니다. 다시 시도해주세요")