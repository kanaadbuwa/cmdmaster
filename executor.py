import subprocess
import shlex

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
        print("Error: Invalid command object")
        return 1, "", "Invalid command object"
    
    shell_command = command_obj["command"]
    description = command_obj.get("description", "No description available")
    
    # Print what we're about to execute
    print(f"Executing: {shell_command}")
    print(f"Description: {description}")
    print("-" * 40)
    
    try:
        # Use subprocess to run the command securely
        # For shell commands that might include pipes or redirections, we need shell=True
        # For simpler commands, we can use shlex.split for better security
        
        if "|" in shell_command or ">" in shell_command or "<" in shell_command:
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
        
        # Print command output
        if process.stdout:
            print("Output:")
            print(process.stdout)
        
        # Print any errors
        if process.stderr:
            print("Error:")
            print(process.stderr)
        
        # Return the results
        return process.returncode, process.stdout, process.stderr
        
    except Exception as e:
        print(f"Failed to execute command: {str(e)}")
        return 1, "", str(e)
