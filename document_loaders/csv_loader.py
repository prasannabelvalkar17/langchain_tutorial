from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("document_loaders/Social_Network_Ads.csv")

documents = loader.load()

# every row is fetched as document so list contains all rows

print(len(documents))  # 400
print(documents[0])  # Print the first document