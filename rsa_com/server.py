import socket
import rsa

# Generate RSA key pair
(pubkey, privkey) = rsa.newkeys(1024)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5)

print("Server listening...")

client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established!")

# Sending public key to client
client_socket.sendall(rsa.PublicKey.save_pkcs1(pubkey))

while True:
    # Receiving encrypted message
    encrypted_msg = client_socket.recv(1024)
    if not encrypted_msg:
        break
    
    # Decrypting the received message
    decrypted_msg = rsa.decrypt(encrypted_msg, privkey).decode()
    print(f"Received message: {decrypted_msg}")

client_socket.close()
