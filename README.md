# 🔐 Check My Password

A simple tool that checks if your password has ever been leaked in a data breach — using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

## ⚙️ How It Works

- Uses the **k-anonymity model** (only the first 5 characters of the password hash are sent to the API)
- Your full password is **never sent over the internet** — it's checked securely
- The script returns how many times (if any) the password was found in public leaks

## 🚀 Usage

### 1. Download the script:

Clone the repo or just download `checkmypass2.py` manually.

```bash
git clone https://github.com/Erolt96/password-checker.git
cd password-checker

Run from cmd:
python checkmypass2.py your_password_here



