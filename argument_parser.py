import argparse

class ArgumentParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='CLI Toolkit to launch developer productivity.')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            '--prompt',
            '-p',
            type=str,
            help='Natural language prompt to generate a CLI command for.',
            metavar='<text>'
        )
        group.add_argument(
            '--chat',
            '-c',
            type=str,
            help='A one-off chat with an LLM that you can prompt from your command line. Does not relate to any existing thread',
            metavar='<text>'
        )
        return parser.parse_args()
