from langchain.chains import ConversationChain

def CreateConversationChainWithMemory(llm, memory, prompt):
    conversation_buf = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=prompt
    )
    return conversation_buf