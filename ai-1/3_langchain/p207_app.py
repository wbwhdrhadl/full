from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["product"],
    template="{product}을 만드는 새로은 회사명을 하나 제안해주세요",
)

# chain = LLMChain(model="gpt-3.5-turbo-instruct", temperature=0.9, prompt=prompt)

chain= LLMChain(
    llm=OpenAI(
        model="gpt-3.5-turbo-instruct", temperature=0.9),
        prompt=prompt
)

print(chain.run("컴퓨터게임"))