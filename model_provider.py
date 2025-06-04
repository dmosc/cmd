from abc import ABC, abstractmethod
from typing import Any, Dict

class ModelProvider(ABC):
    @abstractmethod
    def generate_command(self, prompt: str, context: Dict[str, Any]) -> str:
        """
        Generate a CLI command from a natural language prompt and context.
        """
        pass

class OpenAIModelProvider(ModelProvider):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model

    def generate_command(self, prompt: str, context: Dict[str, Any]) -> str:
        import openai
        openai.api_key = self.api_key
        # Compose the system/context message
        system_message = (
            "You are an assistant that generates safe, concise shell commands based on user intent and the following context: "
            + str(context)
        )
        completion = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,
            temperature=0.2,
        )
        command = completion.choices[0].message.content
        return command.strip() if command else ""