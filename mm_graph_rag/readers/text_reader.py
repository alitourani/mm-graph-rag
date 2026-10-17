from mm_graph_rag.readers.base_reader import BaseReader


class TextReader(BaseReader):
    def read(self, file_path: str) -> dict:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"type": "text", "content": content, "source": file_path}
