import random
from abc import ABC, abstractmethod

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

class NakliLLM(Runnable):
    def __init__(self):
        print('LLM created')

    def invoke(self, input_data):
        return self.predict(input_data)

    def predict(self, prompt):
        #dummy implementation of predict method, returns a random response from a predefined list
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}

class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_data):
        return self.format(input_data)

    def format(self, input_dict):
        return self.template.format(**input_dict)

class NakliStrOutputParser(Runnable):

  def __init__(self):
    pass

  def invoke(self, input_data):
    return input_data['response']

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        result = input_data
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data

## Now actual calling of these all custom runnables

template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])

result = final_chain.invoke({'topic':'cricket'})

print(result) ## will print a random value from the response list in NakliLLM class, as we are not actually generating a joke or explanation.