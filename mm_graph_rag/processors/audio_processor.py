import whisper


class AudioProcessor:
    def __init__(self, model_size: str = "tiny"):
        self.model = whisper.load_model(model_size)

    def process_audio(self, audio_path: str) -> str:
        result = self.model.transcribe(audio_path)
        return result.get("text", "")