from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_AES(key, plaintext):
    backend = default_backend()
    iv = os.urandom(16)  # Generate a random IV (Initialization Vector)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv + ciphertext

def decrypt_AES(key, ciphertext):
    backend = default_backend()
    iv = ciphertext[:16]  # Extract IV from the ciphertext
    ciphertext = ciphertext[16:]  # Remove IV from the ciphertext
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data

# Example usage:
key = b'0123456789abcdef'
plaintext = b'Message'

# Encryption
ciphertext = encrypt_AES(key, plaintext)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt_AES(key, ciphertext)
print("Decrypted text:", decrypted_text.decode('utf-8'))