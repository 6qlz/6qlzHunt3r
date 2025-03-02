from colorama import Fore, Style
import subprocess

def scan(command: str) -> str:
    try:
        # Split only on the first parts of the command, keeping the AI prompt intact
        parts = command.split(' -ai ', 1)  # Split only on first occurrence of -ai
        if len(parts) == 2:
            base_command = parts[0].split()  # Split the command part normally
            ai_prompt = parts[1]  # Keep the prompt part as is
            final_command = base_command + ['-ai', ai_prompt]
        else:
            final_command = command.split()
            
        process = subprocess.run(
            final_command,
            capture_output=True,
            text=True
        )
        
        process.check_returncode()  # Raise CalledProcessError for non-zero exit codes
        
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error executing command: {e.output}{Style.RESET_ALL}")
        return ""
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}")
        return ""

def commands(cmd: str) -> None:
    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error executing command: {e.output}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}")
