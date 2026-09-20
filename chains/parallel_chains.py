from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


llm1=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model1 = ChatHuggingFace(llm=llm1)

llm2=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
)

model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(template="Generate short and simple  notes from the following text: {text}", 
                        input_variables=["text"])

prompt2 = PromptTemplate(template="Generate 5 short questions and answers from the following text: {text}",
                        input_variables=["text"])

prompt3 = PromptTemplate(template="Merge provided notes and quiz into single document: notes {notes} quiz {quiz}",
                        input_variables=["notes", "quiz"])

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'text': "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower. Constructed from 1887 to 1889 as the entrance to the 1889 World's Fair, it was initially criticized by some of France's leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world. The Eiffel Tower is the most-visited paid monument in the world; 6.91 million people ascended it in 2015."})

print(result)

chain.get_graph().print_ascii()