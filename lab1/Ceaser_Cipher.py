msg=input("Enter the String ")
key=int(input("Enter the size of the key "))
encrypt=''
for i in msg:
    if i.isupper():
        encrypt+=chr(((ord(i)+key-65)%26)+65)
    else:
        encrypt+=chr(((ord(i)+key-97)%26)+97)
print('Encrypted Message is ',encrypt)

msg=input("Enter the String ")
key=int(input("Enter the size of the key "))
decrypt=''
for i in msg:
    if i.isupper():
        decrypt+=chr(((ord(i)-key-65)%26)+65)
    else:
        decrypt+=chr(((ord(i)-key-97)%26)+97)
print('Decrypt Message is ',decrypt)