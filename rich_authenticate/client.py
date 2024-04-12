from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import socket

# Generate RSA key pair for the client
client_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
client_public_key = client_private_key.public_key()

# Create a socket object and connect to the server
conn = socket.socket()
conn.connect(("172.16.197.79", 8080))

# Send the client's public key to the server
conn.sendall(client_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
))

# Get message input from the user
message = input("Enter your message: ")

# Sign the message using the client's private key
signature = client_private_key.sign(
    message.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(f"Signature Generated using private key of client: {signature}")

# Prepare data to send (message + signature) as bytes
data_to_send = message.encode() + signature

# Send the data to the server
conn.sendall(data_to_send)

# Close the connection
conn.close()
 