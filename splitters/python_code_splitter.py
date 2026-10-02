from langchain_text_splitters import RecursiveCharacterTextSplitter


code = '''
class MyClass:

    def __init__(self):
        pass
    def my_method(self):
        pass
        
myclass = MyClass()
myclass.my_method()
'''

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=50,
    chunk_overlap=5,
    language="python",
)

chunks = splitter.split_text(code)

print(len(chunks))  # Print the number of code chunks
print(chunks)  # Print the list of code chunks