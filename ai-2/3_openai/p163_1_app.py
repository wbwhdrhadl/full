import openai
import json

def response_from_ChatAI(user_content, r_num=1 ):
    messages = [
        {"role": "user", "content": user_content}
    ]

    response =openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0.8,
        n=r_num
    )

    assistant_replies = []

    for choice in response.choices:
        assistant_replies = choice.message['content']
    return assistant_replies


while True:
    user_content = input("입력하세요 (q를 눌러 종료): ")
    if user_content=='q':
        break
    else:
        res = response_from_ChatAI(user_content,r_num=1)
        for reply in res:
            print("A:", reply, end="\n\n")

