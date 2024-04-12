import socket
import rsa
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('0.0.0.0', 12345))

(pubkey, privkey) = rsa.newkeys(1024)

server_pubkey = rsa.PublicKey.load_pkcs1(client_socket.recv(1024))

message = "Hello, server!"
signature = rsa.sign(message.encode(), privkey, 'SHA-256')

data = pickle.dumps((message.encode(), signature))
client_socket.sendall(data)

client_socket.close()
