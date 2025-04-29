import subprocess
import shlex
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich import box

# Initialize Rich console
console = Console()

def execute_command(command_obj):
    """
    Execute a shell command defined in the command object
    
    Args:
        command_obj (dict): A dictionary containing the command information
            Expected format: {"command": "actual shell command", "description": "command description"}
    
    Returns:
        tuple: A tuple containing (return_code, output, error)
    """
    if not command_obj or "command" not in command_obj:
        console.print("[bold red]Error: Invalid command object[/]")
        return 1, "", "Invalid command object"
    
    shell_command = command_obj["command"]
    
    try:
        # Use subprocess to run the command securely
        # For shell commands that might include pipes or redirections, we need shell=True
        # For simpler commands, we can use shlex.split for better security
        
        if "|" in shell_command or ">" in shell_command or "<" in shell_command or ";" in shell_command:
            # Complex command with pipes or redirections - use shell=True
            process = subprocess.run(
                shell_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
                shell=True
            )
        else:
            # Simple command - split arguments for better security
            cmd_args = shlex.split(shell_command)
            process = subprocess.run(
                cmd_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
        
        # Print command output with nice formatting
        if process.stdout:
            # Try to detect if the output is possibly code or structured data
            if any(marker in process.stdout for marker in ['{}', '[]', '<', '>']):
                # This might be structured data (JSON/XML/etc) - style it as code
                console.print(Panel(
                    Syntax(process.stdout, "text", theme="monokai", line_numbers=False),
                    title="Command Output",
                    border_style="green",
                    box=box.ROUNDED
                ))
            else:
                # Regular text output
                console.print(Panel(
                    process.stdout,
                    title="Command Output",
                    border_style="green",
                    box=box.ROUNDED
                ))
        
        # Print any errors
        if process.stderr:
            console.print(Panel(
                process.stderr,
                title="Error Output",
                border_style="red",
                box=box.ROUNDED
            ))
        
        # Return the results
        return process.returncode, process.stdout, process.stderr
        
    except Exception as e:
        error_msg = str(e)
        console.print(f"[bold red]Failed to execute command: {error_msg}[/]")
        return 1, "", error_msg

# If you want to make this file executable for testing
if __name__ == "__main__":
    # Example command object for testing
    test_command = {
        "command": "ip addr || ifconfig",  # A common command to show IP (works on most Unix systems)
        "description": "Shows network interfaces and IP addresses"
    }
    execute_command(test_command)
