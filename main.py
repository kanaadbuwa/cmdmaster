
import argparse
import subprocess
import yaml
import sys

def load_commands():
    with open("commands_map.yaml", "r") as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Linux Productivity Tool - cmdmaster 🚀")
    parser.add_argument('command_key', help='Command to run')
    args = parser.parse_args()

    commands = load_commands()
    command_key = args.command_key

    if command_key == 'list':
        print("Available Commands:")
        for key in commands.keys():
            print(f"- {key}")
        sys.exit(0)

    if command_key not in commands:
        print(f"❌ Unknown command: '{command_key}'")
        print("🔎 Tip: Run 'python3 main.py list' to see available commands.")
        sys.exit(1)

    command_to_run = commands[command_key]['command']
    print(f"🔹 Running: {command_to_run}")
    subprocess.run(command_to_run, shell=True)

if __name__ == "__main__":
    main()

