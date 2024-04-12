from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import socket

# Generate RSA key pair for the server
private_key_server = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key_server = private_key_server.public_key()

# Serialize the server's public key
server_public_key_pem = public_key_server.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1)

print("Server is listening...")

# Accept a client connection
client_socket, address = server_socket.accept()
print(f"Connection established with {address}")

try:
    # Send the server's public key to the client
    client_socket.sendall(server_public_key_pem)

    while True:
        # Receive encrypted data from the client
        encrypted_data = client_socket.recv(4096)

        if not encrypted_data:
            break

        # Decrypt the received data using the server's private key
        decrypted_data = private_key_server.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        print(f"Received and decrypted data: {decrypted_data.decode()}")

        # Echo back the decrypted message to the client
        client_socket.sendall(decrypted_data)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    client_socket.close()
    server_socket.close()