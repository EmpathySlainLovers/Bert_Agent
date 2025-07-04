import os

print("🎧 Bert is listening to GPT responses. Paste GPT text below.")
print("Only lines starting with '@' will be executed.")
print("Type 'end' alone on a line to run, or 'quit' to exit.\n")

buffer = []

while True:
    line = input()
    
    if line.strip().lower() == "quit":
        print("Bert signing off.")
        break
    
    if line.strip().lower() == "end":
        print("\n🚀 Running tagged commands...\n")
        for cmd in buffer:
            clean_cmd = cmd.lstrip("@").strip()
            try:
                print(f"$ {clean_cmd}")
                result = os.popen(clean_cmd).read()
                print(result)
            except Exception as e:
                print(f"[ERROR] {e}")
        buffer = []
        print("✅ Done. Paste more GPT responses or type 'quit'.\n")
        continue

    if line.strip().startswith("@"):
        buffer.append(line)