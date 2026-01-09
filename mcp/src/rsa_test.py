from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

public_key_pem = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCg0gUguagtMMjJ1KD6fpPkWfofbncqpcdJeVBA764C1VjY3/ttzck6+hKsiAdboQJtugH/X4MjRM8EFe488jdPbh64DO/pmXObWj701lPLuHmZ+H9H1MTCiPRGH8UOdHde9r7ZVl1JsOYQHEf8nLQIkU2ifUhjOHFA+5ReH9gTEQIDAQAB
-----END PUBLIC KEY-----"""

# Load the public key
public_key_obj = RSA.import_key(public_key_pem)

# Create the cipher object using OAEP (Optimal Asymmetric Encryption Padding)
cipher = PKCS1_OAEP.new(public_key_obj)

# The plaintext message
message = "hell rsa"

# Encrypt the message
encrypted_message = cipher.encrypt(message.encode())

# Optionally, you can base64 encode the encrypted message to print it in a readable format
encrypted_message_base64 = base64.b64encode(encrypted_message).decode()

print("Encrypted message (Base64):", encrypted_message_base64)
