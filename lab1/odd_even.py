msg=input("Enter the string ")
even=msg[::2]
odd=msg[1::2]

print("Encrypted string is ", (even+odd))

#Decryption
msg=input("Enter the string to Decrypt ")
mid=(len(msg)+1)//2
even_chars=msg[:mid]
odd_chars=msg[mid:]
decrypted=""
for e,o in zip(even_chars,odd_chars):
    decrypted+=e
    decrypted+=o
if len(msg)%2:
        decrypted+=msg[mid-1]
print(decrypted)
