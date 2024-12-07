# 定义和大模型交互的代码 实现输入密钥，提示即可完成有记忆的对话
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
#1定义函数：定义模型，生成记忆链，调用记忆链，返回记忆链的回答

def memory_chat(key,prompt,memory):
    model = ChatOpenAI(model="gpt-4o",
                       base_url="https://api.aigc369.com/v1",
                       api_key=key
    )
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response['response']

# memory = ConversationBufferMemory(return_message=True)
# print(memory_chat('sk-mVKu3byDEPruqwuWHNCOMqzasZ7DzMdRk2GpLc1Bh6jE5TCF',"我shizs",memory))
# print(memory_chat('sk-mVKu3byDEPruqwuWHNCOMqzasZ7DzMdRk2GpLc1Bh6jE5TCF',"我刚刚问你啥了",memory))
