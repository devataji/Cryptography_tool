# 🔐 Cryptography_tool

Welcome to Cryptography Tool, a sleek and user-friendly Python-based utility for encrypting and decrypting your sensitive messages using the secure Fernet symmetric encryption from the cryptography library. Protect your data with ease and confidence! 🚀

---

## ✨ Features

- 🔑 **Auto-generated secure encryption key**
- 📤 **Encrypt any custom message**
- 📥 **Decrypt using the provided key**
- 💬 **User-friendly command-line prompts**
- 🔒 Built using **Fernet** symmetric encryption for guaranteed security

---


## 📦 Installation
Get started in just a few steps:

1. Clone the Repository:
```bash
git clone https://github.com/devataji/cryptography_tool.git
cd cryptography_tool
 ```
2. Install Dependencies: Ensure you have Python 3.6+ installed, then run:
```bash
pip install cryptography
```
3. Run the Tools:
For encryption: python encryption.py
For decryption: python decryption.py

---

## 📦 Requirements

- Python 3.6+
- [`cryptography`](https://pypi.org/project/cryptography/)

Install with:
```bash
pip install cryptography
```

---

## 📁 Files Included

- `encryption.py` – Script to encrypt your message and generate a secure key.
- `decryption.py` – Script to decrypt the message using the encryption key.

---
## 🛠️ How to Use

### ▶️ Encryption

1. Run the `encryption.py` file:
   ```bash
   python encryption.py
   ```

2. Enter your message when prompted.

3. Copy the **encrypted message** and the **encryption key** displayed.

---

### 🔁 Decryption

1. Run the `decryption.py` file:
   ```bash
   python decryption.py
   ```

2. Paste the **encrypted message** and the **key** you got from encryption.

3. Voila! Your original message is displayed.

---

## 🧪 Example

```bash
$ python encryption.py
input the message you want to encrypt: Hello, world!
Encrypted Message: gAAAAABl...
Encryption Key: WzFKeVVu...

$ python decryption.py
enter the encrypted msg : gAAAAABl...
enter the encryption key : WzFKeVVu...
Decrypted: Hello, world!
```

---
## 🚧 Roadmap

- [ ] Add GUI support
- [ ] Support for file encryption
- [ ] Password-protected encryption key generation

---
