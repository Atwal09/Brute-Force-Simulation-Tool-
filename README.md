# 🔐 Brute Force Login Simulator

This project demonstrates how brute-force attacks work on login forms using Python.  
**Educational only – for ethical hacking and penetration testing learning.**

---

## 📌 Features

- Takes a target URL, username, and password list as inputs
- Sends POST requests to try every password
- Shows success if password is found
- Handles errors and shows status of each attempt

---

## ⚙️ Requirements

- Python 3.x
- `requests` library

```bash
pip install requests


Now how to run~~~~~~~~~~~~~~

🚀 Usage
run -
python brute_force_sim.py <target_url> <username> <wordlist_file>

🔹 Example:

python brute_force_sim.py http://localhost/bruteforce/login.php admin passwords.txt   (📝 Form field names default to username and password.)


## where to use test it (🧪 Legal Testing)
You can test on:

Local servers (e.g. XAMPP, DVWA, custom PHP login)

TryHackMe "Brute It" lab machines

Never test on real sites

⚠️ Disclaimer
This script is for educational and ethical hacking purposes only.
Do NOT use this tool on any live or unauthorized systems.
The author is not responsible for any misuse.
