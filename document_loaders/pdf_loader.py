from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document_loaders/curriculum.pdf")

documents = loader.load()

print(type(documents))  # <class 'list'>
print(len(documents))  # 23
print(type(documents[0]))  # <class 'langchain_core.documents.base.Document'>
print(documents[0].metadata)  # {'source': 'document_loaders/curriculum.pdf', 'page': 0}