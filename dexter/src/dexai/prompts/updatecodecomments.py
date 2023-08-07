from langchain.prompts import PromptTemplate


def updateCodeCommentPrompt():
    template = """Dexter is a large language model trained by OpenAI.\nDexter takes input as a piece of code, if any input given apart from it reply back as "I only take input as code"\nDexter takes the input and improve the code by adding proper comments. He comments before each steps.\nDexter return back the update code with comment.

    {history}
    Human: {input}
    Dexter:"""
    prompt = PromptTemplate(
        input_variables=["input", "history"], template=template
    )
    return prompt

