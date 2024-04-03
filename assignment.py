import random
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# Function to find a primitive root modulo p
def primitive_root(p):
    primitive_roots = []
    for a in range(2, p):
        if pow(a, p - 1, p) == 1:
            primitive_roots.append(a)
    return primitive_roots
    # Generate large prime number p
while True:
    p = random.randint(2**10, 2**12) # Generate a random prime number in a given range
    if is_prime(p):
        break
# Find primitive root modulo p
primitive_roots = primitive_root(p)
g = random.choice(primitive_roots)
print("Prime number (p):", p)
print("Primitive root (g):", g)
# Alice's key generation
a = random.randint(2, p - 1)
A = pow(g, a, p)
# Bob's key generation
b = random.randint(2, p - 1)
B = pow(g, b, p)
# Shared secret computation
s_Alice = pow(B, a, p)
s_Bob = pow(A, b, p)
message = "Is this encoded›‹‹››"
print("Original message:", message)
# One-time pad key generation
otp_key = random.randint(0, 2**len(message)-1)
print("One-time pad key:", otp_key)
# Encryption
cipher_text = ''
for i in range(len(message)):
    cipher_text += chr((ord(message[i]) + otp_key) % 256)
# Decryption
plain_text = ''
for i in range(len(cipher_text)):
    plain_text += chr((ord(cipher_text[i]) - otp_key) % 256)
print("Decrypted message:", plain_text)