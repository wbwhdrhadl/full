import requests
import os
import textwrap

text_file_name = "./data/서연의_이야기.txt"

with open(text_file_name, "r", encoding="utf-8") as f:
    text_data = f.read()

print("[원본 텍스트 파일의 내용 앞부분만 출력하기]")

print(text_data[:200], end="\n\n")

KAGI_API_KEY = os.environ["KAGI_API_KEY"]
api_url = "https://kagi.com/api/v0/summarize"
headers = {"Authorization": "Bot " + KAGI_API_KEY}
data = {"text": text_data, "target_language": "KO"}

r = requests.post(api_url, headers=headers, data=data)

summary = r.json()['data']['output']
short_summary = textwrap.shorten(summary, width=150, placeholder=' [...이하생략...]')
print("- 요약 내용(축약): ", short_summary)