from pydantic import BaseModel


class Config(BaseModel):
    model_name: str = "gpt-4o-mini" # "gpt-4o-mini"
    device: str = "cpu"             # "cuda" or "cpu"
    whisper_model: str = "base"     # "base", "small", "medium", "large"
    graph_depth: int = 2
