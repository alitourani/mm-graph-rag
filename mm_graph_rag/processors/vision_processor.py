import base64
import litellm


class VisionProcessor:
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def process_image(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            b64_img = base64.b64encode(f.read()).decode("utf-8")

        response = litellm.completion(
            model=self.model_name,
            api_key=self.api_key,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Extract all entities, relationships, visual descriptions, and text from this image.",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{b64_img}"},
                        },
                    ],
                }
            ],
        )
        return response.choices[0].message.content
