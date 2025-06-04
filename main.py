import argparse
import os
import subprocess
from providers.openai import OpenAIModelProvider


def get_env_vars():
    return dict(os.environ)

def get_installed_clis():
    clis = set()
    paths = os.environ.get("PATH", "").split(os.pathsep)
    for path in paths:
        if not os.path.isdir(path):
            continue
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                clis.add(entry)
    return sorted(clis)

def main():
    parser = argparse.ArgumentParser(description="Generate CLI commands from natural language using an LLM.")
    parser.add_argument('prompt', type=str, nargs='+', help='Natural language prompt to generate a CLI command for')
    args = parser.parse_args()
    prompt = ' '.join(args.prompt)
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: Please set the OPENAI_API_KEY environment variable.")
        exit(1)
    # Snapshot context
    context = {
        "env_vars": get_env_vars(),
        "installed_clis": get_installed_clis(),
    }
    provider = OpenAIModelProvider(api_key=api_key)
    command = provider.generate_command(prompt, context)
    if command:
        print(f"\nDescription: {command.description}")
        print(f"Command: {command.full_command}")
        if command.flags:
            print("Flags:")
            for flag in command.flags:
                print(f"  --{flag.name} {flag.value}")
        # Offer to run the command
        user_input = input(f"\nWould you like to run this command? [y/N]: ").strip().lower()
        if user_input == 'y':
            try:
                print(f"\nRunning: {command.full_command}\n")
                result = subprocess.run(command.full_command, shell=True, check=True, text=True)
            except subprocess.CalledProcessError as e:
                print(f"\nError running command: {e}")

if __name__ == "__main__":
    main()