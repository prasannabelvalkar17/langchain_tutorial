from dotenv import load_dotenv, parser

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

class FeedbackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback text")

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()
prompt1 = PromptTemplate(template="Classify sentiments of following feedback text into positive or negative \n {feedback}", 
                        input_variables=["feedback"])

classifier_chain = prompt1 | model | parser

result1 = classifier_chain.invoke({'feedback': "The product is amazing and exceeded my expectations!"})

print(result1)
result2 = classifier_chain.invoke({'feedback': "The product is terrible and did not meet my expectations!"})
print(result2)


# We can not predict the output of the model, 
# so we will use a PydanticOutputParser to validate the output and ensure it conforms to the expected format.


parser2 = PydanticOutputParser(pydantic_object=FeedbackSentiment)

prompt1 = PromptTemplate(template="Classify sentiments of following feedback text into positive or negative \n {feedback} \n {format_instructions}", 
                        input_variables=["feedback"],
                        partial_variables={"format_instructions": parser2.get_format_instructions()})

classifier_chain2 = prompt1 | model | parser2

result3 = classifier_chain2.invoke({'feedback': "The product is amazing and exceeded my expectations!"})

print(result3)
result4 = classifier_chain2.invoke({'feedback': "The product is terrible and did not meet my expectations!"})
print(result4)


prompt2 = PromptTemplate(template="Write an appropriate response to the following positive feedback text: {feedback}",
                        input_variables=["feedback"])

prompt3 = PromptTemplate(template="Write an appropriate response to the following negative feedback text: {feedback}",
                        input_variables=["feedback"])

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "The sentiment is neither positive nor negative, please provide valid feedback text.")  # default case in RunnableBranch
)

final_chain = classifier_chain2 | branch_chain

final_chain_result1 = final_chain.invoke({'feedback': "The product is amazing and exceeded my expectations!"})
print(final_chain_result1)

final_chain.get_graph().print_ascii()