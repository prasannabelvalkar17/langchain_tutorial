from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(template="Give me 3 facts about {topic}. \n {format_instructions}", 
                input_variables=["topic"],
                partial_variables={"format_instructions": parser.get_format_instructions()})

chain = template | model | parser

result = chain.invoke({"topic": "Harry Potter"})

print(result)

# structured output parser does not guarantee data validation, 
# it just helps to structure the output in a specific format. 
# If you want to validate the data, you can use pydantic models.