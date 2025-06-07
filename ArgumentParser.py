import argparse

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

        args = parser.parse_args()
        return args.prompt, args.chat
