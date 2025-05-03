from typing import Dict

SUPPORTED_MODELS: Dict[str, str] = {
    "llama3.2-vision:11b": "ollama",
    "gemma3:12b": "ollama",
    "qwen3:32b": "ollama",
    "granite3.2-vision:2b": "ollama",
    "minicpm-v:8b": "ollama",
    "gpt-4o": "openai",
    "gpt-4o-mini": "openai",
    "gemini-2.0-flash": "gemini",
    "gemini-2.5-flash-preview-04-17" : "gemini",   
    "gemini-2.5-pro-preview-03-25" : "gemini",
}
