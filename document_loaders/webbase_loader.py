from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itm387c20f1f5347?pid=MOBHQV9YZGYG64U7&param=7681&pageUID=1790775303890")
documents = loader.load()

print(type(documents))  # <class 'list'>
print(len(documents))  # 1
print(documents[0].metadata)  # {'source': 'https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itm387c20f1f5347?pid=MOBHQV9YZGYG64U7&param=7681&pageUID=1790775303890'}
print(documents[0].page_content)  # The content of the document