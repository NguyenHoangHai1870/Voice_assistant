from app.orchestrator import Orchestrator

orc = Orchestrator()
USER_ID = 1

print("=== TEST CHAT (type 'exit' to quit) ===")

while True:
    text = input("You: ")

    if text.lower() == "exit":
        break

    response = orc.process_text(USER_ID, text)

    print("Bot:", response)
    print("-" * 40)