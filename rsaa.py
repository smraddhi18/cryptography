from Crypto.Util import number

def generate_rsa_keypair(key_size):
    # Generate RSA keypair
    p = number.getPrime(key_size)
    q = number.getPrime(key_size)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = number.inverse(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(plaintext, public_key):
    # RSA encryption
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    # RSA decryption
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Example usage:
public_key, private_key = generate_rsa_keypair(2048)
message = 123456789
encrypted_message = rsa_encrypt(message, public_key)
decrypted_message = rsa_decrypt(encrypted_message, private_key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
