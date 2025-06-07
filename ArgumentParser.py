import argparse

class CLIArgumentParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='CLI Toolkit to launch developer productivity.')
        sub_parser = parser.add_subparsers(dest='command', help='Available commands')

        # Prompt parser
        prompt_parser = sub_parser.add_parser('prompt', help='Natural language prompt to generate a CLI command for.')
        prompt_parser.add_argument('prompt', help='The prompt to be evaluated for command generation.')

        # Chat parser
        chat_parser = sub_parser.add_parser('chat', help='A one-off chat with an LLM that you can prompt from your command line. Does not relate to any existing thread')
        chat_parser.add_argument('chat', help='The prompt to be responded to.')
        
        args = parser.parse_args()
        has_prompt = args.command == 'prompt'
        has_chat = args.command == 'chat'
        prompt = None if not has_prompt else args.prompt
        chat = None if not has_chat else args.chat
        return prompt, chat

