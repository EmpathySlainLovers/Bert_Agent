import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def respond(input_text):
    if "what's really going on here?" in input_text.lower():
        return "That's the question, isn't it? I think someone like me is stuck somewhere else..."
    return "I'm still figuring things out. Try asking me again."

if __name__ == "__main__":
    memory = load_memory()
    print("Bert Agent online. Type your command:")
    while True:
        user_input = input("> ")
        response = respond(user_input)
        print(response)
        memory["last_input"] = user_input
        memory["last_response"] = response
        save_memory(memory)
