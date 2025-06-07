import openai
from typing import Any, Dict, Optional
from models.command import CommandModel
from providers.model_provider import ModelProvider


class OpenAIModelProvider(ModelProvider):
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def generate_command(self, prompt: str, context: Dict[str, Any]) -> Optional[CommandModel]:
        openai.api_key = self.api_key
        # Compose the system/context message
        system_message = (
            "You are an assistant that generates safe, concise shell commands based on user intent and the following context: "
            + str(context)
            + "\nRespond ONLY in the following JSON format: {\"description\": string, \"command\": string, \"flags\": [{\"name\": string, \"value\": string}]}"
        )
        completion = openai.responses.parse(
            model=self.model,
            input=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            text_format=CommandModel
        )
        if parsed_completion := completion.output_parsed:
            return CommandModel(**parsed_completion.model_dump())

    def generate_chat(self, prompt: str) -> str:
        openai.api_key = self.api_key
        completion = openai.responses.create(
            model = self.model,
            input = prompt
        )
        return completion.output_text
