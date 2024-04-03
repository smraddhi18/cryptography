def set_permutation_order(key):
    key_map = {}
    for i, char in enumerate(key):
        key_map[char] = i
    return key_map

def encrypt_message(message, key):
    row, col = len(message) // len(key), len(key)
    if len(message) % col:
        row += 1

    matrix = [['' for _ in range(col)] for _ in range(row)]

    k = 0
    for i in range(row):
        for j in range(col):
            if k < len(message):
                if message[k].isalpha() or message[k] == ' ':
                    matrix[i][j] = message[k]
                    k += 1
                else:
                    matrix[i][j] = '_'
                    k += 1

    key_map = set_permutation_order(key)
    cipher = ''

    for j in range(col):
        for i in range(row):
            if matrix[i][key_map[key[j]]].isalpha() or matrix[i][key_map[key[j]]] == ' ' or matrix[i][key_map[key[j]]] == '_':
                cipher += matrix[i][key_map[key[j]]]

    return cipher

def decrypt_message(cipher, key):
    col = len(key)
    row = len(cipher) // col

    cipher_mat = [['' for _ in range(col)] for _ in range(row)]

    k = 0
    for j in range(col):
        for i in range(row):
            cipher_mat[i][j] = cipher[k]
            k += 1

    key_map = set_permutation_order(key)
    index = 0
    for char in key:
        key_map[char] = index
        index += 1

    dec_cipher = [['' for _ in range(col)] for _ in range(row)]

    k = 0
    for l in range(len(key)):
        j = key_map[key[l]]
        for i in range(row):
            dec_cipher[i][k] = cipher_mat[i][j]
        k += 1

    message = ''
    for i in range(row):
        for j in range(col):
            if dec_cipher[i][j] != '_':
                message += dec_cipher[i][j]

    return message

def main():
    msg = input("\nSend a message:\n").upper()

    key = input("\n\nEnter the key:\n").upper()
    key_map = set_permutation_order(key)

    cipher = encrypt_message(msg, key)
    print("\n\nEncrypted Message:\n", cipher)

    decrypted_msg = decrypt_message(cipher, key)
    print("\n\nDecrypted Message:\n", decrypted_msg)

