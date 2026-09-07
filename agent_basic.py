from dotenv import load_dotenv
import os
from huggingface_hub import login
from transformers import pipeline

# 1. Load .env file (contains your HF_TOKEN)
load_dotenv()

# 2. Log in Hugging Face with your token
hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not hf_token:
    raise SystemExit("No Hugging Face token found. Add  HF_TOKEN=... in your .env file.")
login(token=hf_token)

# 3. Choose a small, free text-generation model
MODEL_ID = "google/flan-t5-base"

# 4. Create a local text2text-generation pipeline
pipe = pipeline(
    task="text2text-generation",
    model=MODEL_ID,
    tokenizer=MODEL_ID
)

# 5. Send one short prompt and print the model's reply
prompt = "Write one short sentence explaining what AI agent does."
result = pipe(prompt, max_new_tokens=100)[0]["generated_text"]
print(result)