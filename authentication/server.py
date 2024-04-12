import socket
import rsa
import pickle

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

# Receiving signed message and signature
data = client_socket.recv(1024)
signed_message, signature = pickle.loads(data)

# Verifying signature
try:
    rsa.verify(signed_message, signature, pubkey)
    print("Signature verified. Message authenticity confirmed.")
except rsa.VerificationError:
    print("Verification failed. Message may be tampered with.")

client_socket.close()
