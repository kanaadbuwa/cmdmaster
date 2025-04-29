from executor import execute_command
import argparse
import yaml
import sys
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich import box

# Initialize rich console
console = Console()

def load_commands():
    try:
        with open("commands_map.yaml", "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        console.print(f"[bold red]Error loading commands: {str(e)}[/]")
        return {}

def display_header():
    """Display a fancy header for cmdmaster"""
    console.print(Panel.fit(
        "[bold blue]CMD[/][bold yellow]MASTER[/] [bold green]🚀[/]", 
        subtitle="[italic]Supercharge your terminal workflow[/]",
        border_style="green"
    ))

def display_commands_table(commands, search_term=None):
    """Display all commands in a rich table"""
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="green")
    table.add_column("Command to Run", style="yellow")
    
    # Track if we found any commands (for search)
    found = False
    
    for key, data in commands.items():
        # If search term is provided, only show matching commands
        if search_term and search_term.lower() not in key.lower():
            continue
            
        found = True
        description = data.get('description', 'No description available')
        command = data.get('command', 'Command not defined')
        table.add_row(key, description, command)
    
    if search_term and not found:
        console.print(f"[bold red]❌ No commands found matching '[italic]{search_term}[/]'[/]")
        return False
        
    console.print(table)
    return True

def display_help():
    """Display a formatted help menu"""
    help_md = """
# 📖 CMDMASTER - Help Menu

## Available Commands

- **list**         : List all available command keys with descriptions.
- **search <kw>**  : Search commands containing the keyword <kw>.
- **info <cmd>**   : Show detailed information about a specific command.
- **help**         : Display this help message.
- **<key>**        : Execute a specific command from the commands_map.yaml.

## Examples

```
python3 main.py list
python3 main.py search ip
python3 main.py info show-ip
python3 main.py show-ip
```

## GO CONQUER THE TERMINAL! 💪
    """
    console.print(Markdown(help_md))

def display_command_info(commands, command):
    """Display detailed information about a specific command"""
    if command not in commands:
        console.print(f"[bold red]❌ Command '[italic]{command}[/]' not found.[/]")
        return
    
    cmd_data = commands[command]
    description = cmd_data.get('description', 'No description available')
    shell_command = cmd_data.get('command', 'Command not defined')
    
    console.print(Panel.fit(
        f"[bold cyan]Command:[/] [yellow]{command}[/]\n\n"
        f"[bold cyan]Description:[/] [green]{description}[/]\n\n"
        f"[bold cyan]Shell Command:[/]\n{Syntax(shell_command, 'bash', theme='monokai')}", 
        title=f"[bold]Command Details: {command}[/]",
        border_style="blue"
    ))

def main():
    parser = argparse.ArgumentParser(description="Linux Productivity Tool - cmdmaster 🚀")
    parser.add_argument('args', nargs='+', help='Command and optional parameters')
    args = parser.parse_args()
    
    # Clear screen for better presentation
    os.system('clear' if os.name == 'posix' else 'cls')
    
    display_header()
    
    commands = load_commands()
    if not commands:
        console.print("[bold red]No commands available. Please check your commands_map.yaml file.[/]")
        sys.exit(1)
    
    command_key = args.args[0]
    
    if command_key == 'list':
        console.print("[bold blue]🛠 Available Commands:[/]")
        display_commands_table(commands)
        sys.exit(0)
    
    if command_key == 'search':
        if len(args.args) < 2:
            console.print("[bold red]⚠️ Please provide a keyword to search.[/]")
            sys.exit(1)
        
        keyword = args.args[1]
        console.print(f"[bold blue]🔍 Search Results for '[italic]{keyword}[/]':[/]")
        if display_commands_table(commands, keyword):
            sys.exit(0)
        else:
            console.print("[yellow]Tip: Try using a different keyword or run 'python3 main.py list' to see all commands.[/]")
            sys.exit(1)
    
    if command_key == 'info':
        if len(args.args) < 2:
            console.print("[bold red]⚠️ Please specify a command to show info for.[/]")
            sys.exit(1)
        
        display_command_info(commands, args.args[1])
        sys.exit(0)
    
    if command_key == 'help':
        display_help()
        sys.exit(0)
    
    if command_key not in commands:
        console.print(f"[bold red]❌ Unknown command: '[italic]{command_key}[/]'[/]")
        console.print("[yellow]🔎 Tip: Run 'python3 main.py list' to see available commands.[/]")
        sys.exit(1)
    
    # Get command data and execute it
    command_data = commands[command_key]
    command_str = command_data.get('command', '')
    description = command_data.get('description', 'No description')
    
    # Show what we're about to do
    console.print(Panel.fit(
        f"[bold green]🔹 Executing:[/] [yellow]{command_str}[/]", 
        subtitle=f"[italic]{description}[/]",
        border_style="blue"
    ))
    
    # Add a separator
    console.print("[bold cyan]─" * 50 + "[/]")
    
    # Execute the command
    return_code, output, error = execute_command(command_data)
    
    # Add a separator after execution
    console.print("[bold cyan]─" * 50 + "[/]")
    
    # Show status
    if return_code == 0:
        console.print("[bold green]✅ Command executed successfully[/]")
    else:
        console.print(f"[bold red]❌ Command failed with exit code: {return_code}[/]")
    
    return return_code

if __name__ == "__main__":
    sys.exit(main())
