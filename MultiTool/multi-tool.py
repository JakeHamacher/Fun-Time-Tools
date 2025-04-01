import subprocess
import json
import os
from datetime import datetime
import argparse

def run_command(command):
    """Runs a shell command and captures the output."""
    try:
        print(f"\nExecuting command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            error_msg = f"Command failed with return code {result.returncode}. Error: {result.stderr}"
            print(f"\n{error_msg}")
            return error_msg
        output = result.stdout.strip()
        print(f"\nCommand output:\n{output}\n")
        return output
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(f"\n{error_msg}")
        return error_msg

def generate_html_report(results, target):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Security Scan Results - {target}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #2c3e50; }}
            .scan-section {{
                margin: 20px 0;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }}
            .scan-title {{
                color: #34495e;
                margin-bottom: 10px;
            }}
            .scan-result {{
                white-space: pre-wrap;
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 3px;
            }}
            .timestamp {{
                color: #7f8c8d;
                font-size: 0.9em;
            }}
            .error {{ color: #e74c3c; }}
        </style>
    </head>
    <body>
        <h1>Security Scan Results</h1>
        <div class="timestamp">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        <p>Target: {target}</p>
    """

    for scan_type, result in results.items():
        html_content += f"""
        <div class="scan-section">
            <h2 class="scan-title">{scan_type}</h2>
            <div class="scan-result">
                {result if not result.startswith("Error") else f'<span class="error">{result}</span>'}
            </div>
        </div>
        """

    html_content += """
    </body>
    </html>
    """
    return html_content

def scan_target(target, skip_scans=None):
    """Runs various security scans on the target and collects results."""
    results = {}
    skip_scans = skip_scans or []

    try:
        print(f"Scanning target: {target}")

        # Validate target input
        if not target or not isinstance(target, str):
            raise ValueError("Invalid target URL/IP provided")

        # Broken Access Control (OWASP ZAP)
        if "zap" not in skip_scans:
            try:
                print("[*] Running OWASP ZAP scan...")
                results["Broken Access Control"] = run_command(f"supports\\ZAP\\zap.bat -cmd -zapit {target}")
            except Exception as e:
                results["Broken Access Control"] = f"Error during ZAP scan: {str(e)}"

        # Cryptographic Failures (testssl.sh)
        if "ssl" not in skip_scans:
            try:
                print("[*] Checking SSL/TLS settings...")
                results["Cryptographic Failures"] = run_command(f"wsl supports/testssl.sh/testssl.sh {target}")
            except Exception as e:
                results["Cryptographic Failures"] = f"Error during SSL check: {str(e)}"

        # Injection (SQL Injection - sqlmap)
        if "sqlmap" not in skip_scans:
            try:
                print("[*] Checking for SQL Injection...")
                results["Injection"] = run_command(f"python3 supports\\sqlmap-dev\\sqlmap.py -u {target} --delay=3 --user-agent='Mozilla//5.0' --batch --level=3 -v 3")
            except Exception as e:                
                results["Injection"] = f"Error during SQL injection check: {str(e)}"

        # Security Misconfiguration (nmap + nikto)
        if "nmap" not in skip_scans:
            try:
                print("[*] Running security misconfiguration checks...")
                results["Security Misconfiguration"] = run_command(f"nmap -T4 -A -v {target}")
            except Exception as e:
                results["Security Misconfiguration"] = f"Error during misconfiguration check: {str(e)}"
        if "nikto" not in skip_scans:
            try:
                print("[*] Running security misconfiguration checks...")
                results["Web Server Misconfigurations"] = run_command(f"perl supports\\nikto\\program\\nikto.pl -h {target} -Tuning 123457890abc -Display V -port 443")
            except Exception as e:
                results["Security Misconfiguration"] = f"Error during misconfiguration check: {str(e)}"


        # SSRF (Nuclei)
        if "nuclei" not in skip_scans:
            try:
                print("[*] Testing for SSRF vulnerabilities...")
                results["SSRF"] = run_command(f"docker run --rm projectdiscovery/nuclei -u {target}")
            except Exception as e:
                results["SSRF"] = f"Error during SSRF check: {str(e)}"

        # Generate and save HTML report
        try:
            html_content = generate_html_report(results, target)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"scan_results_{timestamp}.html"
            
            with open(filename, "w", encoding='utf-8') as file:
                file.write(html_content)
            print(f"\n[✔] Scan completed. Results saved to '{filename}'")
            
            # Also save JSON for backup
            with open(f"scan_results_{timestamp}.json", "w") as file:
                json.dump(results, file, indent=4)
        except Exception as e:
            print(f"\n[!] Error saving results to file: {str(e)}")
            # Attempt to print results to console as fallback
            print("\nScan Results:")
            print(json.dumps(results, indent=4))

    except Exception as e:
        print(f"\n[!] Critical error during scan: {str(e)}")
        results["error"] = str(e)
        # Attempt to save error results
        try:
            html_content = generate_html_report({"Critical Error": str(e)}, target)
            with open("scan_results_error.html", "w", encoding='utf-8') as file:
                file.write(html_content)
        except:
            print("[!] Could not save error results to file")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Security scanning tool that performs multiple vulnerability checks.') 
    parser.add_argument('--skip', '-s', help='Comma-separated list of scans to skip [zap,ssl,sqlmap,nmap,nikto,nuclei]')
    args = parser.parse_args()

    try:
        target_url = input("Enter the target URL/IP: ")
        
        skip_scans = []
        if args.skip:
            skip_scans = [s.strip().lower() for s in args.skip.split(',')]
        else:
            skip_input = input("Enter scans to skip (comma-separated, press enter for none) [zap,ssl,sqlmap,nmap,nikto,nuclei]: ").strip()
            skip_scans = [s.strip().lower() for s in skip_input.split(',')] if skip_input else []
        
        scan_target(target_url, skip_scans)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
    except Exception as e:
        print(f"\n[!] Unexpected error: {str(e)}")
