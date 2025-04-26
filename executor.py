
import subprocess

def execute_command(command):
    try:
        print(f"🔹 Running: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e}")

