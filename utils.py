# from langchain.memory import ConversationBufferMemory
from langchain_openai import  ChatOpenAI
from langchain.chains import ConversationChain
# import os

def cloned_chatgpt(prompt, memory, api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model, memory=memory)

    result = chain.invoke({"input": prompt})
    print(result)
    return result["response"]

# memory = ConversationBufferMemory()
# api_key = os.getenv("OPENAI_API_KEY")
# print(cloned_chatgpt("你知道安溪铁观音吗", memory, api_key))
# print(cloned_chatgpt("我上个问题问了什么", memory, api_key))
