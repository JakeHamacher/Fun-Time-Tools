# HashSlingingSlasher

HashSlingingSlasher is a Python-based password hash cracker that supports multiple attack methods to crack hashed passwords. It leverages dictionary attacks, brute-force attacks, and rainbow table lookups to retrieve plaintext passwords from their hashes.

## Features
- Supports MD5, SHA-1, SHA-256, and SHA-512 hashing algorithms
- Identifies hash type based on hash length
- Performs dictionary attacks using a wordlist
- Executes brute-force attacks with adjustable charset and length
- Generates and loads rainbow tables for efficient lookups
- Detects timing attack vulnerabilities

## Usage
Run the script:
```bash
python3 hss.py
```

Enter the target hash, the path to a wordlist, and optionally a rainbow table path when prompted.

### Dictionary Attack Example
```bash
Enter the hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
Enter the path to the wordlist file: wordlist.txt
Enter the path to the rainbow table file (or press Enter to skip):
```

### Brute-Force Attack Example
```bash
Enter the hash to crack: 5f4dcc3b5aa765d61d8327deb882cf99
Enter the path to the wordlist file: wordlist.txt
Enter the path to the rainbow table file (or press Enter to skip):
```

### Generating a Rainbow Table Example
```bash
hasher = HashSlingingSlasher()
hasher.generate_rainbow_table(charset="abcdefghijklmnopqrstuvwxyz0123456789", length=5, algorithm="md5", output_file="rainbow_table.txt")
```
This will generate a rainbow table for MD5 hashes with a charset of lowercase letters and digits, a length of 5, and save it to `rainbow_table.txt`.