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