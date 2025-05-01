from typing import Dict

SUPPORTED_MODELS: Dict[str, str] = {
    "llava:13b": "ollama",
    "llava:34b": "ollama",
    "llama3.2-vision:11b": "ollama",
    "llama3.2-vision:70b": "ollama",
    "gemma3:12b-it-qat": "ollama",
    "gemma3:27b-it-qat": "ollama",
    "granite3.2-vision:2b": "ollama",
    "minicpm-v:8b": "ollama",
    "gpt-4o": "openai",
    "gpt-4o-mini": "openai",
    "gemini-2.0-flash": "gemini",
    "gemini-2.0-flash-light": "gemini",
    "gemini-2.5-flash-preview-03-25": "gemini",
    "gemini-2.5-pro-preview-03-25": "gemini",
}
