from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["product"],
    template="{product}을 만드는 새로은 회사명을 하나 제안해주세요",
)

print(prompt.format(product="컴퓨터게임"))