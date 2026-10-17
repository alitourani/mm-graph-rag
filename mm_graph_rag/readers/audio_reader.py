from mm_graph_rag.readers.base_reader import BaseReader


class AudioReader(BaseReader):
    def read(self, file_path: str) -> dict:
        return {
            "type": "audio",
            "audio_path": file_path,
            "source": file_path
        }