from langchain.chains import ConversationChain
from langchain.llms import OpenAI

chain = ConversationChain(
    llm=OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0.9
    ),
    verbose=True
)

chain.run("우리집 반려견 이름은 보리입니다.")
chain.predict(input="우리집 반려견 이름은 뭐야?")