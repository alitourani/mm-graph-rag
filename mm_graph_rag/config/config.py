import os
from pydantic import BaseModel


class Config(BaseModel):
    llm_model: str = "gemini/gemini-3.8-flash"
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    whisper_model: str = "tiny"  # tiny, base, small, medium, large
