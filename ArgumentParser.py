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
        group.add_argument('--thread', '-t', nargs="+", type=str, help='Use an existing conversation you\'ve had as part of the context. If empty will use a default thread.', metavar='<text>')
        
        args = parser.parse_args()
        
        thread_id = None
        thread_prompt = None
        if args.thread:
            print(args.thread)
            if '=' in args.text[0]:
                thread_id, thread_prompt = args.thread[0].split('=', 1)[1], args.text[1:]
            else:
                thread_prompt = args.thread

        return args.prompt, args.chat
