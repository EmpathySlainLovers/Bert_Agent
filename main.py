import os

print("Bert is online. Type a command. Type 'exit' to quit.\n")

while True:
    cmd = input("> ")
    if cmd.lower() in ["exit", "quit"]:
        print("Bert signing off.")
        break
    try:
        output = os.popen(cmd).read()
        print(output)
    except Exception as e:
        print(f"[ERROR] {e}")