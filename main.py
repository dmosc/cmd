import os
import subprocess
from providers.deepseek import DeepseekModelProvider
from argument_parser import ArgumentParser


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
    args = ArgumentParser.parse()
    # Snapshot context
    context = {
        "env_vars": get_env_vars(),
        "installed_clis": get_installed_clis(),
    }
    
    try:
        provider = DeepseekModelProvider()
        if args.prompt:
            command = provider.generate_command(args.prompt, context)
            if command:
                print(f"\nDescription: {command.description}")
                print(f"Command: {command.full_command}")
                if command.flags:
                    print("Flags:")
                    for flag in command.flags:
                        print(f"  --{flag.name} {flag.value}")
                # Offer to run the command
                user_input = input(f"Would you like to run this command? [y/N]: ").strip().lower()
                if user_input == 'y':
                    try:
                        print(f"Running: {command.full_command}")
                        result = subprocess.run(command.full_command, shell=True, check=True, text=True)
                    except subprocess.CalledProcessError as e:
                        print(f"Error running command: {e}")
        elif args.chat:
            print(provider.generate_chat(args.chat))
    except RuntimeError as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()
