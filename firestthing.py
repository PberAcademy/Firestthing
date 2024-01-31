import subprocess
import sys
import socket
import os
from datetime import datetime

class OutputParser:
    @staticmethod
    def save_scan_results_to_file(output: str, folder: str, filename: str):
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder, filename)
        with open(file_path, 'w') as f:
            f.write(output)

def run_nmap_scan(target: str, scan_type: str) -> str:
    if scan_type == "normal":
        nmap_options = "-sC"
    elif scan_type == "stealth":
        nmap_options = "-sS -Pn -T4 --randomize-hosts"
    elif scan_type == "deep":
        nmap_options = "-sS -sV -A -T4"
    elif scan_type == "vulnerability":
        nmap_options = "--script vuln"
    else:
        print("Invalid scan type. Supported types: normal, stealth, deep, vulnerability")
        sys.exit(1)

    command = f"nmap {target} {nmap_options}"
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )
        if result.returncode == 0:
            print("Nmap scan completed successfully.")
            return result.stdout
        else:
            print(f"Nmap scan failed with error:\n{result.stderr}")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred while running the Nmap scan: {e}")
        sys.exit(1)

def print_banner():
    banner = """
  ______ _               _     _______ _     _             
 |  ____(_)             | |   |__   __| |   (_)            
 | |__   _ _ __ ___  ___| |_     | |  | |__  _ _ __   __ _ 
 |  __| | | '__/ _ \/ __| __|    | |  | '_ \| | '_ \ / _` |
 | |    | | | |  __/\__ \ |_     | |  | | | | | | | | (_| |
 |_|    |_|_|  \___||___/\__|    |_|  |_| |_|_|_| |_|\__, |
                                                        __/ |
                                                       |___/ 
    PBER ACADEMY - Network Scanning Tool
    DISCLAIMER: This tool is intended for educational and ethical use only.
    Unauthorized scanning of networks and systems may violate applicable laws.
    Users are responsible for compliance with all applicable laws and regulations.
    """

    print(banner)

def main_menu():
    while True:
        print_banner()

        # Get target information from the user
        target = input("Enter the target IP address or hostname: ")

        # Choose Nmap scan type
        print("Choose Nmap scan type:")
        print("1. Normal Scan")
        print("2. Stealth Scan")
        print("3. Deep Scan")
        print("4. Vulnerability Scan")

        choice = input("Enter the number for the desired scan type: ")

        scan_type = ""
        if choice == "1":
            scan_type = "normal"
        elif choice == "2":
            scan_type = "stealth"
        elif choice == "3":
            scan_type = "deep"
        elif choice == "4":
            scan_type = "vulnerability"
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)

        # Run Nmap scan
        nmap_output = run_nmap_scan(target, scan_type)

        # Get current timestamp for appending to the output file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Save scan results to file inside the "output" folder
        OutputParser.save_scan_results_to_file(nmap_output, "output", f"{target}_nmap_results_{timestamp}.txt")

        # Announce completion and output location
        print(f"Nmap scan completed successfully. Results saved to: output/{target}_nmap_results_{timestamp}.txt")

        # Ask if the user wants to perform another scan
        another_scan = input("Do you want to perform another scan? (yes/no): ").lower()

        if another_scan != 'yes':
            print("Bye bye! See you soon.")
            break

if __name__ == "__main__":
    main_menu()
