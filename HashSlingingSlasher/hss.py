import hashlib
import itertools
import string
import time
import os
from typing import Optional

class HashSlingingSlasher:
    def __init__(self):
        self.supported_hashes = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }
        self.rainbow_tables = {}

    def identify_hash(self, hash_string: str) -> Optional[str]:
        hash_lengths = {
            32: 'md5',
            40: 'sha1',
            64: 'sha256',
            128: 'sha512'
        }
        return hash_lengths.get(len(hash_string))

    def generate_hash(self, text: str, algorithm: str) -> str:
        if algorithm not in self.supported_hashes:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        return self.supported_hashes[algorithm](text.encode()).hexdigest()

    def dictionary_attack(self, target_hash: str, wordlist_path: str) -> Optional[str]:
        hash_type = self.identify_hash(target_hash)
        if not hash_type:
            return None

        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                start_time = time.time()
                for word in wordlist:
                    word = word.strip()
                    hashed_word = self.generate_hash(word, hash_type)
                    if hashed_word == target_hash:
                        print(f"Time taken for dictionary attack: {time.time() - start_time:.2f} seconds")
                        print(f"Hash type identified: {hash_type}")
                        return word
            print(f"Time taken for dictionary attack: {time.time() - start_time:.2f} seconds")
        except FileNotFoundError:
            print(f"Error: Wordlist file '{wordlist_path}' not found")
        except Exception as e:
            print(f"Error during dictionary attack: {str(e)}")
        return None

    def brute_force_attack(self, target_hash: str, max_length: int = 8, charset: str = string.ascii_lowercase + string.digits) -> Optional[str]:
        hash_type = self.identify_hash(target_hash)
        if not hash_type:
            return None

        try:
            start_time = time.time()
            total_attempts = 0
            for length in range(1, max_length + 1):
                for guess in itertools.product(charset, repeat=length):
                    word = ''.join(guess)
                    total_attempts += 1
                    if total_attempts % 100000 == 0:
                        elapsed_time = time.time() - start_time
                        print(f"Attempts: {total_attempts}, Time elapsed: {elapsed_time:.2f}s, Rate: {total_attempts/elapsed_time:.2f} attempts/s")
                
                    start_hash = time.time()
                    hashed_word = self.generate_hash(word, hash_type)
                    hash_time = time.time() - start_hash
                
                    if hash_time > 0.1:  # Detect potential timing attack vulnerability
                        print(f"Warning: Hash operation took {hash_time:.2f}s for input '{word}'")
                
                    if hashed_word == target_hash:
                        print(f"Total time taken for brute force: {time.time() - start_time:.2f} seconds")
                        print(f"Total attempts: {total_attempts}")
                        print(f"Hash type identified: {hash_type}")
                        return word
            print(f"Total time taken for brute force: {time.time() - start_time:.2f} seconds")
            print(f"Total attempts: {total_attempts}")
        except Exception as e:
            print(f"Error during brute force attack: {str(e)}")
        return None

    def generate_rainbow_table(self, charset: str, length: int, algorithm: str, output_file: str):
        if algorithm not in self.supported_hashes:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")

        try:
            start_time = time.time()
            with open(output_file, 'w') as f:
                total_entries = 0
                for combination in itertools.product(charset, repeat=length):
                    plaintext = ''.join(combination)
                    hash_value = self.generate_hash(plaintext, algorithm)
                    f.write(f"{hash_value}:{plaintext}\n")
                    total_entries += 1
            print(f"Rainbow table generated in {time.time() - start_time:.2f} seconds")
            print(f"Total entries: {total_entries}")
        except Exception as e:
            print(f"Error generating rainbow table: {str(e)}")

    def load_rainbow_table(self, file_path: str):
        try:
            start_time = time.time()
            self.rainbow_tables.clear()

            # Use binary mode and specify encoding
            with open(file_path, 'rb') as f:
                for line in f:
                    try:
                        # Decode the line manually
                        decoded_line = line.decode('utf-8', errors='ignore').strip()
                        if ':' in decoded_line:
                            hash_value, plaintext = decoded_line.split(':', 1)
                            self.rainbow_tables[hash_value] = plaintext
                    except UnicodeDecodeError:
                        print("Skipped a line due to decoding error.")

            print(f"Rainbow table loaded in {time.time() - start_time:.2f} seconds")
            print(f"Total entries loaded: {len(self.rainbow_tables)}")
        except FileNotFoundError:
            print(f"Error: Rainbow table file '{file_path}' not found")
        except Exception as e:
            print(f"Error loading rainbow table: {str(e)}")

    def crack_with_rainbow_table(self, target_hash: str) -> Optional[str]:
        try:
            start_time = time.time()
            result = self.rainbow_tables.get(target_hash)
            print(f"Rainbow table lookup took {time.time() - start_time:.2f} seconds")
            if result:
                hash_type = self.identify_hash(target_hash)
                print(f"Hash type identified: {hash_type}")
            return result
        except Exception as e:
            print(f"Error during rainbow table lookup: {str(e)}")
            return None

def main():
    hasher = HashSlingingSlasher()

    # Get user input
    target_hash = input("Enter the hash to crack: ")
    wordlist_path = input("Enter the path to the wordlist file: ")
    rainbow_table_path = input("Enter the path to the rainbow table file (or press Enter to skip): ")

    # Dictionary attack
    print("\nTrying dictionary attack...")
    result = hasher.dictionary_attack(target_hash, wordlist_path)
    if result:
        print(f"Found password using dictionary attack: {result}")
        return

    # Rainbow table attack
    if rainbow_table_path:
        print("\nTrying rainbow table attack...")
        hasher.load_rainbow_table(rainbow_table_path)
        result = hasher.crack_with_rainbow_table(target_hash)
        if result:
            print(f"Found password using rainbow table: {result}")
            return

    # Brute force attack
    print("\nTrying brute force attack...")
    result = hasher.brute_force_attack(target_hash)
    if result:
        print(f"Found password using brute force attack: {result}")
    else:
        print("Password not found using any available method")

if __name__ == "__main__":
    main()