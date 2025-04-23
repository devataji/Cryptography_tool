from cryptography.fernet import Fernet

i= input("enter the encrypted msg :")
i.encode()
key =(input("enter the encryption key :"))
x = Fernet(key)

# f= Fernet(your_key)
decrypted_message = x.decrypt(i)
print("Decrypted:", decrypted_message.decode())