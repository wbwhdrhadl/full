import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

engines = ["cecil","agnes","daphne","muriel"]

api_url = "https://kagi.com/api/v0/summarize"
contents_url = "https://www.khan.co.kr/culture/culture-general/article/202212310830021"
headers = {"Authorization": "Bot " + KAGI_API_KEY}

for engine in engines:
    parametes = {"url": contents_url, "engine": engine, "target_language": "KO"}
    r = requests.get(api_url, headers=headers, params=parametes)

    summary = r.json()["data"]["output"]

    shorten_summary = textwrap.shorten(summary, width=150, placeholder=' [... 이하 생락 ...] ')

    print("[요약엔진]", engine)

    print("- 요약 내용(축약) : ", shorten_summary)