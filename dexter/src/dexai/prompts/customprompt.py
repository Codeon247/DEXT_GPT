from langchain.prompts import PromptTemplate


def CustomPrompt(text):
    template = """Dexter is a large language model trained by OpenAI.
    """ + text + """
    {history}
    Human: {input}
    Dexter:"""
    prompt = PromptTemplate(
        input_variables=["input", "history"], template=template
    )
    return prompt
