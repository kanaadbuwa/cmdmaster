
from executor import execute_command
import argparse
import subprocess
import yaml
import sys

def load_commands():
    with open("commands_map.yaml", "r") as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="Linux Productivity Tool - cmdmaster 🚀")
    parser.add_argument('args', nargs='+', help='Command and optional parameters')
    args = parser.parse_args()
    commands = load_commands()
    command_key = args.args[0]
    
    if command_key == 'list':
        print("🛠 Available Commands:")
        for key in commands.keys():
            print(f"- {key}")
        sys.exit(0)
    
    if command_key == 'search':
        if len(args.args) < 2:
            print("⚠️  Please provide a keyword to search.")
            sys.exit(1)
        
        keyword = args.args[1].lower()
        print(f"🔍 Search Results for '{keyword}':")
        found = False
        for key in commands.keys():
            if keyword in key.lower():
                print(f"- {key}")
                found = True
        if not found:
            print("❌ No matching commands found.")
        sys.exit(0)
    
    if command_key == 'help':
        print("""
📖 CMDMASTER - Help Menu
Commands available:
- list        : List all available command keys.
- search <kw> : Search commands containing the keyword <kw>.
- <key>       : Execute a specific command from the commands_map.yaml.
Examples:
  python3 main.py list
  python3 main.py search ip
  python3 main.py show-ip
GO CONQUER THE LINUX    
        """)
        sys.exit(0)
    
    if command_key not in commands:
        print(f"❌ Unknown command: '{command_key}'")
        print("🔎 Tip: Run 'python3 main.py list' to see available commands.")
        sys.exit(1)
    
    # Get command data and execute it
    command_data = commands[command_key]
    
    # Use the execute_command function from executor.py
    return_code, output, error = execute_command(command_data)

if __name__ == "__main__":
    main()
