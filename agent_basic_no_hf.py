from transformers import pipeline

# 1. Modelo público sin token, coder instructivo (mejor para código y general)
MODEL_ID = "Qwen/Qwen2.5-Coder-1.5B-Instruct"

# 2. Create local pipeline (CPU, no HF login required)
pipe = pipeline(
    task="text-generation",
    model=MODEL_ID,
    tokenizer=MODEL_ID,
    device=-1,
)

print("Agent ready! Type a question, or 'quit' to stop.\n")

# Harness generalista (código y conocimiento)
HARNESS = (
    "Eres un asistente útil, preciso y conciso. "
    "Responde siempre en español. "
    "Si es código, entrega solo el código correcto con explicación breve de 1 línea. "
    "Si no es código, responde en una frase clara.\n"
    "Pregunta: {q}\nRespuesta:"
)

while True:
    try:
        user_input = input("> ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue

        prompt = HARNESS.format(q=user_input)
        # Qwen Coder funciona mejor con sampling moderado
        result = pipe(prompt, max_new_tokens=180, do_sample=True, temperature=0.6, top_p=0.9, repetition_penalty=1.1)[0]["generated_text"]
        # Extrae solo la respuesta después de "Respuesta:"
        answer = result[len(prompt):].strip() if result.startswith(prompt) else result.strip()
        print(f"\n Agent: {answer}\n")
    except KeyboardInterrupt:
        print("\n(Stopped) Goodbye!")
        break
