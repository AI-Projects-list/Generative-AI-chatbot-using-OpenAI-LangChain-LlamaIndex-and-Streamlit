from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

def init_index(data_dir):
    reader = SimpleDirectoryReader(data_dir)
    documents = reader.load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    return index

def get_chat_response(query, index, chat_history):
    retriever = index.as_retriever()
    llm = ChatOpenAI(model_name="gpt-4")
    chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever)
    response = chain.run({"question": query, "chat_history": chat_history})
    return response