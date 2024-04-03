def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char
    return ciphertext


def rail_fence_encrypt(plaintext, num_rows):
    rails = [""] * num_rows
    direction = 1  # 1 for down, -1 for up
    row = 0

    for char in plaintext:
        rails[row] += char
        row += direction

        if row == num_rows - 1 or row == 0:
            direction *= -1

    return "".join(rails)


def caesar_rail_fence_encrypt(message, caesar_shift, rail_fence_rows):
    caesar_cipher = caesar_cipher_encrypt(message, caesar_shift)
    rail_fence_cipher = rail_fence_encrypt(caesar_cipher, rail_fence_rows)
    return rail_fence_cipher


def rail_fence_decrypt(ciphertext, num_rows):
    rails = [""] * num_rows
    direction = 1
    row = 0

    for char in ciphertext:
        rails[row] += "*"
        row += direction

        if row == num_rows - 1 or row == 0:
            direction *= -1

    index = 0
    for i in range(num_rows):
        for j in range(len(rails[i])):
            rails[i] = rails[i][:j] + ciphertext[index] + rails[i][j + 1 :]
            index += 1

    plaintext = ""
    direction = 1
    row = 0

    for i in range(len(ciphertext)):
        plaintext += rails[row][0]
        rails[row] = rails[row][1:]
        row += direction

        if row == num_rows - 1 or row == 0:
            direction *= -1

    return plaintext


def caesar_rail_fence_decrypt(ciphertext, caesar_shift, rail_fence_rows):
    rail_fence_decrypted = rail_fence_decrypt(ciphertext, rail_fence_rows)
    caesar_decrypted = caesar_cipher_encrypt(rail_fence_decrypted, -caesar_shift)
    return caesar_decrypted


message = "We are discovered. Save yourself"
shift_amount = 3
num_rail_fence_rows = 2

encrypted_message = caesar_rail_fence_encrypt(
    message, shift_amount, num_rail_fence_rows
)
print("Encrypted:", encrypted_message)

decrypted_message = caesar_rail_fence_decrypt(
    encrypted_message, shift_amount, num_rail_fence_rows
)
print("Decrypted:", decrypted_message)
