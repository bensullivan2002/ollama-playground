import ollama


def chat_with_ollama():
    print("Welcome to Ollama Chat! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Ollama: Goodbye!")
            break

        response = ollama.generate(model='llama3', prompt=user_input)
        print("Ollama: ", response['response'])


if __name__ == "__main__":
    chat_with_ollama()
