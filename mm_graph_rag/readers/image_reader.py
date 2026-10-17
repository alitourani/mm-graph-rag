import base64
from PIL import Image
from mm_graph_rag.readers.base_reader import BaseReader


class ImageReader(BaseReader):
    def read(self, file_path: str) -> dict:
        # Validate image integrity
        with Image.open(file_path) as img:
            img.verify()
            
        with open(file_path, "rb") as f:
            b64_data = base64.b64encode(f.read()).decode("utf-8")
            
        return {
            "type": "image",
            "base64_data": b64_data,
            "source": file_path
        }