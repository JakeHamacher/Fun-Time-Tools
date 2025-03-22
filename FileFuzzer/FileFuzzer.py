import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import os

def encrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        
        # Derive a key from the password
        salt = get_random_bytes(16)
        key = PBKDF2(password, salt, dkLen=32)
        
        # Encrypt the file data with AES
        cipher_aes = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(file_data)
        
        # Save the encrypted data, salt, and original file extension
        file_extension = os.path.splitext(file_path)[1]
        encrypted_file_path = f"{os.path.splitext(file_path)[0]}_enc"
        with open(encrypted_file_path, 'wb') as f:
            f.write(salt)
            f.write(cipher_aes.nonce)
            f.write(tag)
            f.write(file_extension.encode('utf-8') + b'\x00')  # Add null byte as delimiter
            f.write(ciphertext)
        
        messagebox.showinfo("Success", f"File encrypted successfully: {encrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during encryption: {e}")

def decrypt_file(encrypted_file_path, password):
    try:
        with open(encrypted_file_path, 'rb') as f:
            salt = f.read(16)
            nonce = f.read(16)
            tag = f.read(16)
            file_extension = b''
            while True:
                byte = f.read(1)
                if byte == b'\x00':
                    break
                file_extension += byte
            ciphertext = f.read()
        
        # Derive the key from the password
        key = PBKDF2(password, salt, dkLen=32)
        
        # Decrypt the data with AES
        cipher_aes = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        
        decrypted_file_path = f"{os.path.splitext(encrypted_file_path)[0]}_dec{file_extension.decode('utf-8')}"
        with open(decrypted_file_path, 'wb') as f:
            f.write(data)
        
        messagebox.showinfo("Success", f"File decrypted successfully: {decrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during decryption: {e}")

def select_file_to_encrypt():
    file_path = filedialog.askopenfilename()
    if file_path:
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        if password:
            encrypt_file(file_path, password)

def select_file_to_decrypt():
    encrypted_file_path = filedialog.askopenfilename(title="Select Encrypted File")
    if encrypted_file_path:
        password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
        if password:
            decrypt_file(encrypted_file_path, password)

# GUI setup
root = tk.Tk()
root.title("File Encryptor/Decryptor")

# Apply dark theme
root.configure(bg='#2e2e2e')
frame = tk.Frame(root, padx=10, pady=10, bg='#2e2e2e')
frame.pack(padx=10, pady=10)

button_style = {'bg': '#4d4d4d', 'fg': 'white', 'activebackground': '#666666', 'activeforeground': 'white'}

encrypt_button = tk.Button(frame, text="Select File to Encrypt", command=select_file_to_encrypt, **button_style)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(frame, text="Select File to Decrypt", command=select_file_to_decrypt, **button_style)
decrypt_button.pack(pady=5)

root.mainloop()
