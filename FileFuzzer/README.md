# File Encryptor/Decryptor

## Overview

This is a simple file encryption and decryption tool with a graphical user interface (GUI) built using Tkinter. It uses AES encryption (EAX mode) to secure files and stores essential metadata to ensure successful decryption.

## Features

- **AES Encryption (EAX Mode):** Ensures confidentiality and integrity.
- **Password-Based Encryption:** Uses PBKDF2 key derivation with a random salt.
- **Secure File Handling:** Encrypts/decrypts a variety of filetypes.
- **Dark Theme GUI:** Provides a visually appealing dark theme for the interface.

## Requirements

- Python 3.x

## Installation

1. Install Python if not already installed.
2. Install required dependencies if not already installed.
3. Run the script:
    ```sh
    python FileFuzzer.py
    ```

## Usage

### Encrypt a File

1. Click "Select File to Encrypt" in the GUI.
2. Choose the file you want to encrypt.
3. Enter a password for encryption.
4. The encrypted file will be saved with `_enc` added to the filename.

### Decrypt a File

1. Click "Select File to Decrypt" in the GUI.
2. Choose the encrypted file.
3. Enter the correct password.
4. The decrypted file will be restored with its original extension.

## Security Notes

- Use a strong password to ensure security.
- If you lose the password, decryption is impossible.
- Each encryption generates a new salt, making attacks more difficult.