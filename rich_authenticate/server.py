from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import socket

# Create a socket object
s = socket.socket()

# Bind the socket to a specific IP address and port
s.bind(("172.16.197.79", 8080))

# Listen for incoming connections
s.listen(1)
print("Server is listening...")

# Accept a connection from a client
conn, addr = s.accept()

# Load the client's public key from received data
client_public_key = serialization.load_pem_public_key(
    conn.recv(4096),
    backend=default_backend()
)

# Receive data containing message and signature
data_received = conn.recv(4096)
message = data_received[:-256]  # Extract the message part
signature = data_received[-256:]  # Extract the signature part

print(f"Signature received: {signature}")

# Verify the signature using the client's public key
try:
    client_public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is VALID.")
    print("Message received:", message.decode())

except Exception as e:
    print(f"Signature is INVALID: {e}")

finally:
    # Close the connection and socket
    conn.close()
    s.close()