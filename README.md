# 🔐 cryptography_tool

Welcome to **cryptography_tool** — a simple yet powerful command-line tool for encrypting and decrypting messages using Python's `cryptography` library. Whether you're learning about data security or need a quick encryption utility, this tool has you covered!

---

## ✨ Features

- 🔑 **Auto-generated secure encryption key**
- 📤 **Encrypt any custom message**
- 📥 **Decrypt using the provided key**
- 💬 **User-friendly command-line prompts**
- 🔒 Built using **Fernet** symmetric encryption for guaranteed security

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

## 🚧 Roadmap

- [ ] Add GUI support
- [ ] Support for file encryption
- [ ] Password-protected encryption key generation

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues](https://github.com/your-username/cryptography_tool/issues) or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
