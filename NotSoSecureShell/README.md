# Not So Secure Shell

## Description

The Not So Secure Shell is a Python script that attempts to gain access to an SSH server using a list of usernames and passwords. It performs a dictionary attack by trying different username-password combinations and reports successful login attempts.

## Features

- **Automated SSH Login Attempts**: Uses the Paramiko library to try logging into an SSH server.
- **Dictionary Attack**: Reads usernames and passwords from files to attempt authentication.
- **Batch Username Support**: Accepts a single username or a file containing multiple usernames.
- **Customizable Port**: Allows specifying a different SSH port (default is 22).

## Usage

Run the script with the following arguments:

```sh
python ssh_attack.py <ip> <username_or_file> <password_file> [-p <port>]
```

### Arguments:
- `<ip>`: Target IP address.
- `<username_or_file>`: Single username or a file containing usernames (one per line).
- `<password_file>`: File containing passwords (one per line).
- `-p, --port` (optional): SSH port (default is 22).

### Example Usages:

1. Attempt with a single username:
   ```sh
   python ssh_attack.py 192.168.1.100 root passwords.txt
   ```

2. Attempt with multiple usernames from a file:
   ```sh
   python ssh_attack.py 192.168.1.100 usernames.txt passwords.txt
   ```

3. Specify a different SSH port:
   ```sh
   python ssh_attack.py 192.168.1.100 admin passwords.txt -p 2222
   ```

## Legal Disclaimer

This tool is intended for educational and ethical penetration testing purposes **only**. Unauthorized use against systems without explicit permission is illegal and punishable by law. Use responsibly.
