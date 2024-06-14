from llama_index import download_loader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, LangChainEmbedding
from llama_index.readers import BeautifulSoupReader
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import Document

loader = BeautifulSoupReader()

documents = loader.load_data(urls=["https://openai.com/blog/planning-for-agi-and-beyong"])
print("Documents loaded successfully")
print(f"Loaded documents: {documents}")

document_objects = [Document(text=doc.text) for doc in documents]

embed_model = LangChainEmbedding(HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
))

print("Embedding Model initialized successfully")

llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"))
print("LLM Predictor initialized successfully")

service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, embed_model=embed_model)
print("Service Context initialized successfully")

index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
print("Index initialized successfully")

query_engine = index.as_query_engine()
print("Query Engine initialized successfully")

query = "이 웹페이지에서 전하고 싶은 말은 무엇인가요? 한국어로 답해주세요"
response = query_engine.query(query)
print(f"Query: {query}", end="\n")
print(f"Response: {response}", end="\n")
print(f"source_nodes: {response.source_nodes}", end="\n")
