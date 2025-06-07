import argparse

class CLIArgumentParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='CLI Toolkit to launch developer productivity.')
        sub_parser = parser.add_subparsers(dest='command', help='Available commands')
        # Create a mutually exclusive group
        group = parser.add_mutually_exclusive_group(required=True)
    
        # Add `--prompt` or `-p` argument
        group.add_argument('--prompt', '-p', type=str, help='Provide a prompt text', metavar='<text>')
    
        # Add `--chat` or `-c` argument
        group.add_argument('--chat', '-c', type=str, help='Provide chat text', metavar='<text>')
    
        args = parser.parse_args()
        return args.prompt, args.chat
