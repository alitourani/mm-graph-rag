from abc import ABC, abstractmethod


class BaseReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> dict:
        """Returns a standardized dictionary payload containing extracted media/text."""
        pass