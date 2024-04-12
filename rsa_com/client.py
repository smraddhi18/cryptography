import socket
import rsa

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('0.0.0.0', 12345))

# Receiving public key from server
server_pubkey = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))

# Encrypting message with server's public key
message = "Hello, server!"
encrypted_msg = rsa.encrypt(message.encode(), server_pubkey)
client_socket.sendall(encrypted_msg)

client_socket.close()
