from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import socket

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5)

print("Server listening for connections...")

while True:
    client_socket, address = server_socket.accept()
    print("Connection from: ", address)

    client_socket.send(public_key)

    try:
        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break

            cipher_rsa = PKCS1_OAEP.new(key)
            decrypted_message = cipher_rsa.decrypt(encrypted_message)

            print("Message received: ", decrypted_message.decode())
    except KeyboardInterrupt:
        break
    finally:
        client_socket.close()

server_socket.close()