from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

memory = ConversationBufferMemory(
    llm = ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature = 0
    ),
    max_token_limit = 50,
    return_messages = True
)

memory.save_context({"input":"배고파"},{"ouput": "어디가서 밥 먹을까?"})
memory.save_context({"input": "라면 먹으러 가자"}, {"output":"지하철 앞에 있는 분식점으로 가자"})
memory.save_context({"input": "그럼 출발!"}, {"output": "OK!!"})

print(memory.load_memory_variables({}))