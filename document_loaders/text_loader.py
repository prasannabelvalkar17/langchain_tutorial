from langchain_community.document_loaders import TextLoader

loader = TextLoader("document_loaders/harry.txt", encoding="utf-8")
documents = loader.load()

print(type(documents))  # <class 'list'>
print(len(documents))  # 1
print(type(documents[0]))  # <class 'langchain_core.documents.base.Document'>
print(documents[0].metadata)  # {'source': 'document_loaders/harry.txt'}
print(documents[0].page_content)  # The content of the document