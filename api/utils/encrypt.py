from cryptography.fernet import Fernet
import os

key = os.environ['ENCRYPTION_KEY']
f = Fernet(key)
keep_going = True

while keep_going:
    value_to_encryp = input("Enter a value to encrypt: ")
    encrypted_value = f.encrypt(value_to_encryp.encode())

    print(encrypted_value)

    keep_going_input = input("Keep going?(y/n): ")
    if keep_going_input != 'y':
        keep_going = False
