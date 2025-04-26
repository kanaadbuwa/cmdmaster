
import argparse
from executor import execute_command
import yaml

def load_commands():
    with open("command_map.yaml", "r") as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Linux Productivity Tool - cmdmaster 🚀")
    parser.add_argument('action', help='Action to perform')
    args = parser.parse_args()

    commands = load_commands()

    if args.action in commands:
        execute_command(commands[args.action])
    else:
        print(f"❌ Unknown action: {args.action}")
        print("Use one of:", ', '.join(commands.keys()))

if __name__ == "__main__":
    main()


