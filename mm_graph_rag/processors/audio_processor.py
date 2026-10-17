import whisper
from mm_graph_rag.processors.base_processor import BaseProcessor


class AudioProcessor(BaseProcessor):
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def process(self, raw_payload: dict) -> str:
        result = self.model.transcribe(raw_payload["audio_path"])
        return result.get("text", "")