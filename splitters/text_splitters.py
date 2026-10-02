from langchain_text_splitters import CharacterTextSplitter

text = '''
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
'''

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=5,
    separator='')

splits = splitter.split_text(text)

# print(len(splits))  # Print the number of text chunks
# print(splits)  # Print the list of text chunks


# Now lets try to to load PDF and split it into chunks using the same splitter.
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document_loaders/curriculum.pdf")

documents = loader.load()

split_pdf = splitter.split_documents(documents)

print(len(split_pdf))  # Print the number of document chunks
print(type(split_pdf))  # Print the type of the split documents
print(split_pdf[0])  # Print the first document chunk