from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(template="Give me name, age, and email of fictional character {character_name}. \n {format_instructions}", 
                input_variables=["character_name"],
                partial_variables={"format_instructions": parser.get_format_instructions()})

print(template.format(character_name="Harry Potter"))
chain = template | model | parser

result = chain.invoke({"character_name": "Harry Potter"})

print(result)