import os
from cryptography.fernet import Fernet
import time
# AJlGnd

parent_dir = input("Enter Your Directory: ")
key_dir = input("Enter Your key Directory(default(enter)): ")
if key_dir == '':
    key_dir = os.path.join(os.getcwd(), "DefaultKey.key")
listall = os.listdir(parent_dir)

with open(key_dir, 'rb') as FileKey:
    key = FileKey.read()
fernet = Fernet(key)

encrypted = []
for files1 in listall:
    split_tup = os.path.splitext(files1)
    file_extension = split_tup[1]
    dirchk = os.path.isdir(os.path.join(parent_dir, files1))

    if files1 != "pyenc.py" and file_extension != ".key" and dirchk == False:
        encrypted.append(files1)

y = 1
length_encrypted = len(encrypted)
cmd = input("Encrypt OR Decrypt (d,e): ").lower()

if cmd == "e":

    for files in encrypted:
        percentage = int((y / length_encrypted) * 100)

        with open(os.path.join(parent_dir, files), 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)

        with open(os.path.join(parent_dir, files), 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            y += 1
        print(f"{percentage}%")
else:

    for files in encrypted:
        percentage = int((y / length_encrypted) * 100)


        with open(os.path.join(parent_dir, files), 'rb') as file:
            original = file.read()
        decrypted = fernet.decrypt(original)

        with open(os.path.join(parent_dir, files), 'wb') as encrypted_file:
            encrypted_file.write(decrypted)
            y += 1
        print(f"{percentage}%")
print("Done")
time.sleep(1)

