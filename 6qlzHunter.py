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

def payloads(prompt: str):
    location = os.path.join(os.path.dirname(__file__), "Prompts", f"{prompt}.txt")
    with open(location, "r") as file:
        prompts = [line.strip() for line in file.readlines() if line.strip()]
        payload = "\n".join(prompts).replace('"', '\\"')
    return f'"{payload}"'

def target_list(file: str):
    try:
        with open(file, "r") as file:
            targets = [x.strip() for x in file.readlines()]
        return targets
    except Exception as e:
        print(Fore.RED + f"Error reading target list file: {str(e)}")
        start()

def run_scan_with_progress(input_file: str, payload: str, scan_type: str):
    print(Fore.CYAN + f"\nStarting {scan_type} scan..." + Style.RESET_ALL)
    with tqdm(total=100,
              desc="Scanning",
              bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
        output = scan(f"nuclei -list {input_file} -ai {payload} -silent")
        for i in range(100):
            time.sleep(0.1)
            pbar.update(1)
    if output:
        results = parse_nuclei_output(output)
        report_gen = ReportGenerator()
        report_gen.generate_report(results, scan_type, ["html", "json", "csv"])
        return output # Return output for further use if needed
    return None

def emails():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("emails")
    output = run_scan_with_progress(input_file, payload, "Emails")
    if not output:
        print(Fore.RED + "No results found")

def low_hanging_fruits():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("lowhangingfruits")
    output = run_scan_with_progress(input_file, payload, "Low Hanging Fruits")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def sensitive_data_exposure():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("sensitivedataexposure")
    output = run_scan_with_progress(input_file, payload, "Sensitive Data Exposure")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def sql_injection():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("sqli")
    output = run_scan_with_progress(input_file, payload, "SQL Injection")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def cross_site_scripting():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("xss")
    output = run_scan_with_progress(input_file, payload, "Cross Site Scripting")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def server_side_request_forgery():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("ssrf")
    output = run_scan_with_progress(input_file, payload, "Server Side Request Forgery")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def local_and_remote_file_inclusion():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("fileinclusion")
    output = run_scan_with_progress(input_file, payload, "Local and Remote File Inclusion")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def command_injection():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("commandinjection")
    output = run_scan_with_progress(input_file, payload, "Command Injection")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def xxe():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("xxe")
    output = run_scan_with_progress(input_file, payload, "XXE")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def host_header_injection():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("hostheaderinjection")
    output = run_scan_with_progress(input_file, payload, "Host Header Injection")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def cloud_security_issues():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("cloudsecurity")
    output = run_scan_with_progress(input_file, payload, "Cloud Security Issues")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def web_cache_poisoning():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("webcachepoisoning")
    output = run_scan_with_progress(input_file, payload, "Web Cache Poisoning")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def security_misconfigurations():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("securitymisconfig")
    output = run_scan_with_progress(input_file, payload, "Security Misconfigurations")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def hardcoded_credentials():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("hardcodedcredentials")
    output = run_scan_with_progress(input_file, payload, "Hardcoded Credentials")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)


def deserialization():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("deserialization")
    output = run_scan_with_progress(input_file, payload, "Deserialization")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def idor():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("idor")
    output = run_scan_with_progress(input_file, payload, "IDOR")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def race_condition():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("racecondition")
    output = run_scan_with_progress(input_file, payload, "Race Condition")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

def websocket():
    input_file = input(Fore.WHITE + "Enter the target list file: ")
    targets = target_list(input_file)
    payload = payloads("websocket")
    output = run_scan_with_progress(input_file, payload, "WebSocket")
    if not output:
        print(Fore.RED + "No results found")
    else:
        parse_nuclei_output(output)

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
            print (Fore.RED + "  [" + Fore.WHITE + "99" + Fore.RED + "]" + Fore.WHITE + " Exit")
            print ("\n")

            prompt = input(Fore.RED + "6qlzHunt3r~" + Fore.WHITE + "# ")

            if prompt == "00":
                low_hanging_fruits()
            elif prompt == "01":
                sensitive_data_exposure()
            elif prompt == "02":
                sql_injection()
            elif prompt == "03":
                cross_site_scripting()
            elif prompt == "04":
                server_side_request_forgery()
            elif prompt == "05":
                local_and_remote_file_inclusion()
            elif prompt == "06":
                command_injection()
            elif prompt == "07":
                xxe()
            elif prompt == "08":
                host_header_injection()
            elif prompt == "09":
                cloud_security_issues()
            elif prompt == "10":
                web_cache_poisoning()
            elif prompt == "11":
                emails()
            elif prompt == "12":
                security_misconfigurations()
            elif prompt == "13":
                hardcoded_credentials()
            elif prompt == "14":
                deserialization()
            elif prompt == "15":
                idor()
            elif prompt == "16":
                race_condition()
            elif prompt == "17":
                websocket()
            elif prompt == "99" or prompt == "99" or prompt == "exit" or prompt == "quit":
                break
            else:
                print(Fore.RED + "Invalid option")

    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting...")
        exit()

if __name__ == "__main__":
    start()
