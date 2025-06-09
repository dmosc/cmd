import openai
from typing import Any, Dict, Optional
from models.command import CommandModel
from providers.model_provider import ModelProvider
from providers.thread_mapper import ThreadMapper
import time

class OpenAIModelProvider(ModelProvider):
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key
        # Create an assistant for thread conversations
        self.assistant = openai.beta.assistants.create(
            name="Command Line Assistant",
            instructions="You are a helpful assistant that helps users with command line tasks and general questions.",
            model=self.model
        )
        self.assistant_id = self.assistant.id

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

    def wait_for_run_completion(self, thread_id: str, run_id: str) -> None:
        """Wait for a run to complete and handle any errors."""
        while True:
            run_status = openai.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run_id
            )
            if run_status.status == 'completed':
                break
            elif run_status.status in ['failed', 'cancelled', 'expired']:
                raise Exception(f"Run failed with status: {run_status.status}")
            time.sleep(1)  # Wait a second before checking again

    def generate_thread(self, thread_id: str, prompt: str) -> str:
        openai.api_key = self.api_key
        if not thread_id:
            thread_id = "default"
        thread_id_map = ThreadMapper.get_thread_map()
        self.create_thread_if_does_not_exist(thread_id, thread_id_map)
        updated_thread_id_map = ThreadMapper.get_thread_map()
        real_id = updated_thread_id_map[thread_id]
        message = openai.beta.threads.messages.create(
            thread_id=real_id,
            role='user',
            content=prompt
        )
        run = openai.beta.threads.runs.create(
            thread_id=real_id,
            assistant_id=self.assistant_id
        )
        
        # Wait for the run to complete
        self.wait_for_run_completion(real_id, run.id)
            
        # Get the latest message after the run is complete
        messages = openai.beta.threads.messages.list(thread_id=real_id)
        latest_message = messages.data[0]
        return latest_message.content[0].text.value

    def create_thread_if_does_not_exist(self, t_id: str, thread_id_map):
        if t_id not in thread_id_map.keys():
            response = openai.beta.threads.create()
            ThreadMapper.map_new_thread(user_specified_id = t_id, platform_generated_id = response.id)
