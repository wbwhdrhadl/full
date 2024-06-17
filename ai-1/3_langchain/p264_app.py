import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

wolfram_alpha_appid = os.environ.get("WOLFRAM_ALPHA_APPID")

tools = load_tools(["wlofram-alpha"])

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages = True
)

agent = initialize_agent(
    agent="zero-shot-react-description",
    llm = ChatOpenAI(
        model = "get-3.5-turbo",
        temperature = 0
    ),
    tools = tools,
    memory = memory,
    verbose = True
)

query = "How many kilometers is the distance between seoul and busan?"
print(query)
print(agent.run(query))