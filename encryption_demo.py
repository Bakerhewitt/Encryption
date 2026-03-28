#Run with: python encryption_demo.py

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

message = "Hello, L. Did you know? Gods of Death love apples. (Death Note reference)"

print("Original message:", message)
print()

#Symmetric encryption:

print("--- Symmetric Encryption ---")

key = Fernet.generate_key()         
f   = Fernet(key)

encrypted = f.encrypt(message.encode())
decrypted = f.decrypt(encrypted).decode()

print("Key:      ", key.decode())
print("Encrypted:", encrypted.decode())
print("Decrypted:", decrypted)
print()

#Asymmetric encryption:

print("--- Asymmetric Encryption ---")

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key  = private_key.public_key()

encrypted2 = public_key.encrypt(
    message.encode(),
    padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
decrypted2 = private_key.decrypt(
    encrypted2,
    padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
).decode()

print("Encrypted (hex):", encrypted2.hex()[:60], "...")
print("Decrypted:", decrypted2)