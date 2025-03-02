from colorama import Fore, Style
from Modules.sub_proc import scan
from Nuclei.parser import parse_nuclei_output
from tqdm import tqdm
import os
import requests
import subprocess
import time
from Modules.report_generator import ReportGenerator
from packaging import version
from concurrent.futures import ThreadPoolExecutor

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

banner = fr"""

   _____       __      __  __            __ _____     
  / ___/____ _/ /___  / / / /_  ______  / /|__  /_____
 / __ \/ __ `/ /_  / / /_/ / / / / __ \/ __//_ </ ___/
/ /_/ / /_/ / / / /_/ __  / /_/ / / / / /____/ / /    
\____/\__, /_/ /___/_/ /_/\__,_/_/ /_/\__/____/_/     
        /_/                                           

   Made by @6qlz                     v.1
"""

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(Fore.RED + f"Error reading file: {str(e)}")
        return None

def payloads(prompt: str):
    location = os.path.join(os.path.dirname(__file__), "Prompts", f"{prompt}.txt")
    return "\n".join(read_file(location)).replace('"', '\\"')

def run_scan(target, payload, scan_type):
    output = scan(f"nuclei -target {target} -ai {payload} -silent")
    if output:
        results = parse_nuclei_output(output)
        report_gen = ReportGenerator()
        report_gen.generate_report(results, scan_type, ["html", "json", "csv"])
        return results
    return None

def run_scan_with_progress(targets, payload, scan_type):
    print(Fore.CYAN + f"\nStarting {scan_type} scan..." + Style.RESET_ALL)
    with tqdm(total=len(targets),
              desc="Scanning",
              bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(run_scan, target, payload, scan_type) for target in targets]
            for future in futures:
                future.result()
                pbar.update(1)

def scan_type_function(scan_type, prompt):
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = read_file(input_file)
    if targets:
        payload = payloads(prompt)
        run_scan_with_progress(targets, payload, scan_type)
    else:
        print(Fore.RED + "No targets found")

def check_for_updates():
    current_version = "1.0.0"  # Update this to the current version of your tool
    repo_owner = "6qlz"
    repo_name = "6qlzHunt3r"

    try:
        response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest")
        response.raise_for_status()  # Raise an exception for HTTP errors
        latest_release = response.json()
        latest_version = latest_release["tag_name"]
        release_notes = latest_release["body"]

        if version.parse(latest_version) > version.parse(current_version):
            print(Fore.GREEN + f"\nA new version of 6qlzHunt3r is available: {latest_version}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Release Notes:\n{release_notes}\n" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "\nYou are using the latest version of 6qlzHunt3r." + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"\nFailed to check for updates: {str(e)}" + Style.RESET_ALL)

def start():
    try:
        clear_terminal()
        while True:
            print(Fore.RED + banner)
            print (Fore.RED + "  [" + Fore.WHITE + "00" + Fore.RED + "]" + Fore.WHITE + " Low Hanging Fruits")
            print (Fore.RED + "  [" + Fore.WHITE + "01" + Fore.RED + "]" + Fore.WHITE + " Sensitive Data Exposure")
            print (Fore.RED + "  [" + Fore.WHITE + "02" + Fore.RED + "]" + Fore.WHITE + " SQL Injection")
            print (Fore.RED + "  [" + Fore.WHITE + "03" + Fore.RED + "]" + Fore.WHITE + " Cross Site Scripting")
            print (Fore.RED + "  [" + Fore.WHITE + "04" + Fore.RED + "]" + Fore.WHITE + " Server Side Request Forgery")
            print (Fore.RED + "  [" + Fore.WHITE + "05" + Fore.RED + "]" + Fore.WHITE + " File Inclusion")
            print (Fore.RED + "  [" + Fore.WHITE + "06" + Fore.RED + "]" + Fore.WHITE + " Command Injection")
            print (Fore.RED + "  [" + Fore.WHITE + "07" + Fore.RED + "]" + Fore.WHITE + " XML External Entity")
            print (Fore.RED + "  [" + Fore.WHITE + "08" + Fore.RED + "]" + Fore.WHITE + " Host Header Injection")
            print (Fore.RED + "  [" + Fore.WHITE + "09" + Fore.RED + "]" + Fore.WHITE + " Cloud Security Issues")
            print (Fore.RED + "  [" + Fore.WHITE + "10" + Fore.RED + "]" + Fore.WHITE + " Web Cache Poisoning")
            print (Fore.RED + "  [" + Fore.WHITE + "11" + Fore.RED + "]" + Fore.WHITE + " Emails")
            print (Fore.RED + "  [" + Fore.WHITE + "12" + Fore.RED + "]" + Fore.WHITE + " Security Misconfigurations")
            print (Fore.RED + "  [" + Fore.WHITE + "13" + Fore.RED + "]" + Fore.WHITE + " Hardcoded Credentials")
            print (Fore.RED + "  [" + Fore.WHITE + "14" + Fore.RED + "]" + Fore.WHITE + " Deserialization")
            print (Fore.RED + "  [" + Fore.WHITE + "15" + Fore.RED + "]" + Fore.WHITE + " IDOR")
            print (Fore.RED + "  [" + Fore.WHITE + "16" + Fore.RED + "]" + Fore.WHITE + " Race Condition")
            print (Fore.RED + "  [" + Fore.WHITE + "17" + Fore.RED + "]" + Fore.WHITE + " WebSocket")
            print (Fore.RED + "  [" + Fore.WHITE + "98" + Fore.RED + "]" + Fore.WHITE + " Check for Updates")
            print (Fore.RED + "  [" + Fore.WHITE + "99" + Fore.RED + "]" + Fore.WHITE + " Exit")
            print ("\n")

            prompt = input(Fore.RED + "6qlzHunt3r~" + Fore.WHITE + "# ")

            scan_type_map = {
                "00": ("Low Hanging Fruits", "lowhangingfruits"),
                "01": ("Sensitive Data Exposure", "sensitivedataexposure"),
                "02": ("SQL Injection", "sqli"),
                "03": ("Cross Site Scripting", "xss"),
                "04": ("Server Side Request Forgery", "ssrf"),
                "05": ("File Inclusion", "fileinclusion"),
                "06": ("Command Injection", "commandinjection"),
                "07": ("XML External Entity", "xxe"),
                "08": ("Host Header Injection", "hostheaderinjection"),
                "09": ("Cloud Security Issues", "cloudsecurity"),
                "10": ("Web Cache Poisoning", "webcachepoisoning"),
                "11": ("Emails", "emails"),
                "12": ("Security Misconfigurations", "securitymisconfig"),
                "13": ("Hardcoded Credentials", "hardcodedcredentials"),
                "14": ("Deserialization", "deserialization"),
                "15": ("IDOR", "idor"),
                "16": ("Race Condition", "racecondition"),
                "17": ("WebSocket", "websocket")
            }

            if prompt in scan_type_map:
                scan_type_function(*scan_type_map[prompt])
            elif prompt == "98":
                check_for_updates()
            elif prompt in ["99", "exit", "quit"]:
                break
            else:
                print(Fore.RED + "Invalid option")

    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting...")
        exit()

if __name__ == "__main__":
    start()
