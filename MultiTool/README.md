# Security Scanning MultiTool

## Overview

The Security Scanning MultiTool is a comprehensive vulnerability assessment tool designed to perform multiple security checks on a target IP or URL from Windows environments. It integrates several industry-standard security testing tools and generates detailed HTML and JSON reports summarizing the findings.

This is essentially a pocket-knife or a multitool for security testing. By that I mean it can do a lot but it won't do any of it very well and it will probably take a long time to do it. You'd be better off using a dedicated tool for each individual task but this was fun to make regardless :)

The tool's methodology and test cases are aligned with parts of the OWASP Top 10 security risks framework, providing coverage for common web application vulnerabilities.

## Features

- Broken Access Control (OWASP ZAP)
- Cryptographic Failures (testssl.sh)
- Injection (SQL Injection using sqlmap)
- Security Misconfiguration (nmap + nikto)
- SSRF Detection (Nuclei)

## Prerequisites

Ensure the following tools are installed and accessible in your environment:

- OWASP ZAP
- testssl.sh (via WSL for Windows users)
- sqlmap
- nmap
- nikto
- Docker (for Nuclei)
- Python

## Usage

```
python3 multi-tool.py [--skip scans]
```

`--skip scans`: Optional. Comma-separated list of scans to skip. Valid options are:
- zap
- ssl
- sqlmap
- nmap
- nikto
- nuclei

### Example:
```
python3 multi-tool.py --skip zap,sqlmap
```

## Running the Tool

1. Execute the script: `python3 multi-tool.py`
2. Enter the target IP or URL when prompted.
3. Optionally, specify scans to skip.
4. View the generated HTML and JSON reports in the current directory.

## Example Output

After running a scan, results are stored as:
- `scan_results_YYYYMMDD_HHMMSS.html` - HTML report
- `scan_results_YYYYMMDD_HHMMSS.json` - JSON report

## Error Handling

If any scan fails, the tool displays an error message and logs it in the report.