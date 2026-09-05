from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation"
    )

    return ChatHuggingFace(llm=llm)

model = get_llm()

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    # chat_history.append(f"You: {user_input}")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": result.content})
    # chat_history.append(f"AI: {result.content}")
    print(f"AI: {result.content}")

print(f"\nChat History: {chat_history}")