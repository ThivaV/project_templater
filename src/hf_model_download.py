from huggingface_hub import hf_hub_download

# Set model information
repo_id = 'TheBloke/Llama-2-7B-Chat-GGUF'
model_file = 'llama-2-7b-chat.Q8_0.gguf'

model_save_path = 'llama-2-7b-chat.Q8_0.gguf'

# Download model
model_path = hf_hub_download(repo_id=repo_id, filename=model_file, cache_dir=model_save_path, force_download=False)

print(f'Model downloaded to: {model_path}')