import requests
import os
import textwrap

KAGI_API_KEY = os.environ["KAGI_API_KEY"]

api_url = "https://kagi.com/api/v0/summarize"
contents_url = "https://edition.cnn.com/2023/03/26/middleeast/israel-judicial-overhaul-legislation-intl/index.html"
headers = {"Authorization": "Bot " + KAGI_API_KEY}
parametes = {"url": contents_url,"target_language": "KO"}


r = requests.get(api_url, headers=headers, params=parametes)

# print(r)

# print(r.json())

summary = r.json()["data"]["output"]

shorten_summary = textwrap.shorten(summary, width=150, placeholder=' [... 이하 생락 ...] ')

print("- 요약 내용(축약) : ", shorten_summary)