from transformers import pipeline

# 1. Modelo público sin token, español nativo (GPT2)
MODEL_ID = "datificate/gpt2-small-spanish"

# 2. Create local pipeline (CPU, no HF login required)
pipe = pipeline(
    task="text-generation",
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
