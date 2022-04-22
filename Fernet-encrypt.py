import os
from cryptography.fernet import Fernet

text = input("Enter text to encrypt: ")
btext = bytes(text ,'utf-8')

key = Fernet.generate_key()

with open('/tmp/filekey.key', 'wb') as filekey:
    filekey.write(key)

os.chmod('/tmp/filekey.key', 0o600)



cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(btext)
cipher_text = cipher_text.decode("utf-8")

print(cipher_text)
