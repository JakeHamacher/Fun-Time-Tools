# Fun Time Tools

Welcome to the Fun Time Tools project! This repository contains a collection of useful Python-based tools for different tasks. Currently, it includes the following two subprojects:

- **Metadata Extractor Tool**: Extracts metadata from a variety of file types, including images, PDFs, and MS Word files.
- **IP Geolocation Tool**: Allows batch processing of IP addresses to retrieve their geolocation information.
- **Port Manager**: A GUI tool to monitor and manage open network ports on Windows systems.
- **Not So Secure Shell**: Attempts to gain access to an SSH server using a list of usernames and passwords.
- **File Fuzzer**: Encryption and decryption tool with a graphical user interface.
- **CTF MultiTool**: A comprehensive vulnerability assessment tool that combines various security testing tools such as OWASP ZAP, testssl.sh, sqlmap, nmap, nikto, and Nuclei.

## Features

### Metadata Extractor Tool

- Images: Extract metadata from JPEG images (EXIF data like camera model, date taken, etc.).
- PDFs: Extract metadata such as author, title, producer, and subject.
- Text Files: Extract metadata like word count, line count, and file encoding.
- Returns metadata in a structured CSV format.

### IP Geolocation Tool

- Perform geolocation lookups for single or multiple IP addresses.
- Batch processing of IP addresses from a text file.
- Output results in CSV.
- Uses ipinfo.io API for retrieving geolocation data.

### Port Manager

- View Open Ports: Displays a list of currently open ports with details including local and foreign addresses, connection state, process ID (PID), and associated service.
- Close Ports: Allows users to terminate processes associated with open ports using a single button click.
- Service Identification: Fetches and displays service details related to a process using preloaded CSV files.
- Admin Privileges Check: Ensures the application runs with administrator privileges for necessary permissions.

### Not So Secure Shell
- Automated SSH Login Attempts: Uses the Paramiko library to try logging into an SSH server.
- Dictionary Attack: Reads usernames and passwords from files to attempt authentication.
- Batch Username Support: Accepts a single username or a file containing multiple usernames.
- Customizable Port: Allows specifying a different SSH port (default is 22).

### File Fuzzer
- AES Encryption (EAX Mode): Ensures confidentiality and integrity.
- Password-Based Encryption: Uses PBKDF2 key derivation with a random salt.
- Secure File Handling: Encrypts/decrypts a variety of filetypes.
- Dark Theme GUI: Provides a "visually appealing" dark theme for the interface.

### CTF MultiTool
- Broken Access Control (OWASP ZAP): Tests for authentication and authorization vulnerabilities.
- Cryptographic Failures (testssl.sh): Identifies SSL/TLS configuration issues and weaknesses.
- Injection (SQL Injection using sqlmap): Automates detection and exploitation of SQL injection flaws.
- Security Misconfiguration (nmap + nikto): Scans for common security misconfigurations and vulnerabilities.
- SSRF Detection (Nuclei): Identifies Server-Side Request Forgery vulnerabilities using templates.
## Installation

To get started, you'll need to clone the repository and install the required dependencies.

Clone the repository:

```bash
git clone https://github.com/JakeHamacher/Fun-Time-Tools.git
git submodule init
git submodule update
```

Navigate to the project folder:

```bash
cd Fun-Time-Tools
```

Follow the specific installation instructions for each subproject in their own README.

## Contributing

Feel free to fork this repository and contribute improvements, bug fixes, or new features via pull requests. If you have any ideas or suggestions, don't hesitate to open an issue!
