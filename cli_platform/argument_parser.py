import argparse
from dataclasses import dataclass

@dataclass(frozen=True)
class Thread:
    thread_id: str
    thread_prompt: str

class CLIArgumentParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='CLI Toolkit to launch developer productivity.')
        # Create a mutually exclusive group
        group = parser.add_mutually_exclusive_group(required=True)
    
        # Add `--prompt` or `-p` argument
        group.add_argument('--prompt', '-p', type=str, help='Natural language prompt to generate a CLI command for.', metavar='<text>')
    
        # Add `--chat` or `-c` argument
        group.add_argument('--chat', '-c', type=str, help='A one-off chat with an LLM that you can prompt from your command line. Does not relate to any existing thread', metavar='<text>')

        # Add `--thread` or `-t` argument
        group.add_argument('--thread', '-t', nargs='?', help='The thread id you want to use in this conversation, if none is provided will use a default thread', metavar='<text>')
        parser.add_argument('thread_content', nargs='?', type=str, help='The chat content or prompt for your thread conversation. Must be used in conjuction with the --thread flag.')

        args = parser.parse_args()
        
        thread = None
        if args.thread:
            # If thread_content is provided, thread contains the ID and thread_content contains the prompt
            if args.thread_content:
                thread_id = args.thread
                thread_prompt = args.thread_content
            # If thread_content is None, thread actually contains the prompt (no ID specified)
            else:
                thread_id = None
                thread_prompt = args.thread
            
            thread = Thread(thread_id, thread_prompt)

        return args.prompt, args.chat, thread
