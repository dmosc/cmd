from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel

class ModelProvider(ABC):
    @abstractmethod
    def generate_command(self, prompt: str, context: Dict[str, Any]) -> BaseModel:
        """
        Generate a CLI command from a natural language prompt and context.
        """
        pass

    @abstractmethod
    def generate_chat(self, prompt: str) -> str:
        """
        Generate a CLI one-off chat with the model.
        """
        pass
