import ollama

ollama_client = ollama.Client()
model = "llama3.2"

prompt = "What is Artificial Intelligence?"
output = ollama_client.generate(model=model, prompt=prompt)
print(output)