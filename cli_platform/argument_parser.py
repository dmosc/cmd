import argparse
from dataclasses import dataclass

class CLIArgumentParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='CLI Toolkit to launch developer productivity.')
        
        # Add the default positional prompt argument
        parser.add_argument('prompt', nargs='?', type=str, help='Natural language prompt or question to process', metavar='<prompt>')
        
        # Create a mutually exclusive group for special modes
        group = parser.add_mutually_exclusive_group()
        
        # Add `--force_command` or `-f` argument
        group.add_argument('--force_command', '-f', action='store_true', help='Force the prompt to be interpreted as a command generation request')
        
        # Add `--thread` or `-t` argument with optional thread ID
        group.add_argument('--thread', '-t', nargs='?', const='default-chat', help='Use a specific thread ID for the conversation. If no ID is provided, uses default-chat', metavar='<thread_id>')

        args = parser.parse_args()

        return args.prompt, args.force_command, args.thread
