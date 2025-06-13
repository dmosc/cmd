from openai import OpenAI
import requests
from typing import Any, Dict, Optional
from models.command import CommandModel
from providers.model_provider import ModelProvider


class DeepseekModelProvider(ModelProvider):
    BASE_URL = "http://localhost:11434"

    def __init__(self, model: str = "deepseek-r1"):
        self.model = model
        if not self._check_server_health():
            raise RuntimeError(
                f"Expecting an Ollama server to be running in {self.BASE_URL}; "
                "If installed, run 'ollama serve' to start serving a model locally "
                "or install Ollama following instructions at https://ollama.com."
            )
        self.client = OpenAI(base_url=f"{self.BASE_URL}/v1")

    def _check_server_health(self) -> bool:
        try:
            response = requests.get(self.BASE_URL)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def generate_command(self, prompt: str, context: Dict[str, Any]) -> Optional[CommandModel]:
        # Compose the system/context message
        system_message = (
            "You are an assistant that generates safe, concise shell commands based on user intent and the following context: "
            + str(context)
            + "\nRespond ONLY in the following JSON format: {\"description\": string, \"command\": string, \"flags\": [{\"name\": string, \"value\": string}]}"
        )
        completion = self.client.beta.chat.completions.parse(
            model=self.model,
            temperature=0,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            response_format=CommandModel
        )
        if parsed_completion := completion.choices[0].message.parsed:
            return CommandModel(**parsed_completion.model_dump())

    def generate_chat(self, prompt: str) -> str:
        completion = self.client.responses.create(
            model = self.model,
            input = prompt
        )
        return completion.output_text
