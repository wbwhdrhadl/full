from openai import OpenAI
client = OpenAI()

prompt="좋아하는 음식은 뭐야?"
response = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal::9Y47jYv0",
    message=[{"role":"usuer","content":prompt}],
)

print(response.choices[0].message.content.strip())