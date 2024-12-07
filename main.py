# chat聊天的网页设计
# 1导入库 2导入组件：标题，侧边栏，聊天信息（字典储存消息，chat_messages()输出消息） 3输入聊天消息，条件判断
# 挑战：如何一键刷新，重新开启会话

import streamlit as st
from utills import memory_chat
from langchain.memory import ConversationBufferMemory

st.title("嘉子专属聊天小助手小晨为您服务！❤❤❤❤")
# st.title("聊天小助手为您服务！")


with st.sidebar:
    key = st.text_input("",type="password")
    st.markdown("[API密钥用完了点这里哦！](https://api.aigc369.com)")
    button = st.button("重新开启会话")

if button:
    with st.spinner("加载中"):
        st.session_state['memory'] = ConversationBufferMemory()
        st.session_state['messages']=[{"role":"ai","content":"想和小晨说什么呢"}]

if 'memory' not in st.session_state:
    st.session_state['memory'] = ConversationBufferMemory()
    st.session_state['messages']=[{"role":"ai","content":"想和小晨说什么呢"}]
for message in st.session_state['messages']:
    st.chat_message(message['role']).write(message['content'])

ask = st.chat_input()
if ask:
    if ask and not key:
        st.info("请先输入API密钥哦")
        st.stop()
    st.session_state['messages'].append({"role":"human","content":ask})
    st.chat_message("human").write(ask)
    with st.spinner("小晨还在思考中"):
        res = memory_chat(key,ask,st.session_state['memory'])
    st.session_state['messages'].append({"role":"ai","content":res})
    st.chat_message('ai').write(res)


