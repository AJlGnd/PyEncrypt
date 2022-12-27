import os
from cryptography.fernet import Fernet
# AJlGnd
parent_dir = input("Enter Your Directory: ")
listall = os.listdir(parent_dir)

with open('EncKey.key', 'rb') as FileKey:
    key = FileKey.read()
fernet = Fernet(key)

encrypted = []
for files1 in listall:
    split_tup = os.path.splitext(files1)
    file_extension = split_tup[1]

    if files1 != "pyenc.py" and file_extension != ".key" and file_extension != '':
        encrypted.append(files1)

y = 0
length_encrypted = len(encrypted)
cmd = input("Encrypt OR Decrypt(d,e)/>> ").lower()

if cmd == "e":

    for files in encrypted:
        percentage = int((y / length_encrypted) * 100)
        print(f"{percentage}%")

        with open(os.path.join(parent_dir, files), 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)

        with open(os.path.join(parent_dir, files), 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            y += 1
else:

    for files in encrypted:
        percentage = int((y / length_encrypted) * 100)
        print(f"{percentage}%")

        with open(os.path.join(parent_dir, files), 'rb') as file:
            original = file.read()
        decrypted = fernet.decrypt(original)

        with open(os.path.join(parent_dir, files), 'wb') as encrypted_file:
            encrypted_file.write(decrypted)
            y += 1
print("Done")
