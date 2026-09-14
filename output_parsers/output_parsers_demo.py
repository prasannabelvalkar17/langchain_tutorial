from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(template="Write detailed report on {word}?", input_variables=["word"])

template2 = PromptTemplate(template="Write a 5 line summary on {text}", 
                input_variables=["text"])

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"word": "Samsung Galaxy S24 Ultra"})

print(result)