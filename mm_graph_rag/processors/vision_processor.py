import litellm
from mm_graph_rag.processors.base_processor import BaseProcessor


class VisionProcessor(BaseProcessor):
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name

    def process(self, raw_payload: dict) -> str:
        b64_data = raw_payload["base64_data"]
        response = litellm.completion(
            model=self.model_name,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe key objects, entities, relations, and text visible in this image."},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_data}"}}
                ]
            }]
        )
        return response.choices[0].message.content