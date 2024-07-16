import ollama


def summarise_text(text):
    prompt = f"Please summarize the following text in a concise manner:\n\n{text}\n\nSummary:"
    response = ollama.generate(model='llama3', prompt=prompt)
    return response['response']
