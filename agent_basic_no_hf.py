from transformers import pipeline

# 1. Choose a small, free text2text-generation model (public, no token needed)
MODEL_ID = "google/flan-t5-base"

# 2. Create local pipeline (CPU, no HF login required)
pipe = pipeline(
    task="text2text-generation",
    model=MODEL_ID,
    tokenizer=MODEL_ID,
    device=-1,
)

print("Agent ready! Type a question, or 'quit' to stop.\n")

while True:
    try:
        user_input = input("> ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        result = pipe(user_input, max_new_tokens=100)[0]["generated_text"]
        print(f"\n Agent: {result}\n")
    except KeyboardInterrupt:
        print("\n(Stopped) Goodbye!")
        break
