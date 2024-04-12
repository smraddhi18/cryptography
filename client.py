from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '172.16.97.239'
server_port = 12345

client_socket.connect((server_ip, server_port))
print("Connected to server.")

server_public_key = client_socket.recv(1024)

key = RSA.import_key(server_public_key)

cipher_rsa = PKCS1_OAEP.new(key)

try:
    while True:
        message = input("Type the message or exit")
        if message.lower() == 'exit':
            break

        encrypted_message = cipher_rsa.encrypt(message.encode())

        client_socket.send(encrypted_message)
        print("Message sent to server.")

finally:
    client_socket.close()