from cryptography.fernet import Fernet


key = Fernet.generate_key()
f= Fernet(key)



message = input('input the mesage you want to encrypt: ').encode()
encrypted_message = f.encrypt(message)
print("Encrypted Message: ", encrypted_message.decode())
# print(" and here the encrypt key")

print("Encryption Key: ", key.decode())