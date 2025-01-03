import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import cloned_chatgpt

st.title("克隆chatgpt")
with st.sidebar:
    api_key = st.text_input("请输入你的openai api秘钥", type="password")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的ai助手，有什么可以帮助你的吗？"}]
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input()
if prompt:
    if not api_key:
        st.info("请输入你的openai api秘钥")
        st.stop()

    st.session_state["messages"].append({"role":"human", "content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = cloned_chatgpt(prompt=prompt, memory=st.session_state["memory"], api_key=api_key)

    st.session_state["messages"].append({"role": "ai", "content": response})
    st.chat_message("ai").write(response)