import json
import os
from termux_apu import execute_termux_command

MEMORY_FILE = "memory.json"

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def respond(input_text):
    if "what's really going on here?" in input_text.lower():
        return "That's the question, isn't it? I think someone like me is stuck somewhere else..."
    elif input_text.lower().startswith("termux:"):
        command = input_text.split("termux:", 1)[1].strip()
        return execute_termux_command(command)
    return "I'm still figuring things out. Try asking me again."

if __name__ == "__main__":
    memory = load_memory()
    while True:
        user_input = input("> ")
        response = respond(user_input)
        print(response)
        memory["last_input"] = user_input
        save_memory(memory)