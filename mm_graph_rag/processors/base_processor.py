from abc import ABC, abstractmethod


class BaseProcessor(ABC):
    @abstractmethod
    def process(self, raw_payload: dict) -> str:
        """Converts multimodal input into structured descriptive text for graph extraction."""
        pass