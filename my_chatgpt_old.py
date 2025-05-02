

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

def summarize_text(text, prompt):
    #if __name__ == "__main__":
        template = prompt + ":\n" + text
        print (template)
        final_prompt = ChatPromptTemplate.from_template(template)
    
        llm = ChatOpenAI()
        chain = (
            {"text": RunnablePassthrough()}
            | final_prompt
            | llm
            | StrOutputParser()
        )
        return chain.invoke(text)
