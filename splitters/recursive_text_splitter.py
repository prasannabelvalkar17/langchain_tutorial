from langchain_text_splitters import RecursiveCharacterTextSplitter

text = '''
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50, 
    chunk_overlap=5,
    length_function=len,
    # separators=["\n\n", "\n", " ", ""]
)

splits = splitter.split_text(text)

print(len(splits))  # Print the number of text chunks
print(splits)  # Print the list of text chunks