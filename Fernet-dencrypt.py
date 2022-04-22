from cryptography.fernet import Fernet

text = input("Enter string to dencrypt: ")
btext = bytes(text ,'utf-8')

# opening the key
with open('/tmp/filekey.key', 'rb') as filekey:
    key = filekey.read()

cipher_suite = Fernet(key)

plain_text = cipher_suite.decrypt(btext)
plain_text = plain_text.decode("utf-8")

print(plain_text)
