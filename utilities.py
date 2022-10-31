from threading import stack_size
import hashlib
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from pathlib import Path
import os

# Check if there is a lowercase letter in the string
def check_lower(st):
    for c in st:
        if c.islower():
            return True
    return False

# Check if there is an uppercase letter in the string
def check_upper(st):
    for c in st:
        if c.isupper():
            return True
    return False

# Check if there is a number in the string
def check_number(st):
    for c in st:
        if c.isdigit():
            return True
    return False

# Check if there is a special charactar in the string
def check_symbol(st):
    special_characters = "!@#$%^&*()-+?_=,<>/\""
    if any(c in special_characters for c in st):
        return True
    return False

# Has the string, convert from bytes to string format and return the string
def hash_string(st, salt):
    #key = hashlib.pbkdf2_hmac('sha256', st.encode('utf-8'), salt, 100000)
    key = PBKDF2(st, salt, 64, count=1000000, hmac_hash_module=SHA512)
    key_str = key.decode('ISO-8859-1')
    return key_str

# Scan if the user file exists 
def user_file_scan():
    file = Path('users.json')
    if file.is_file():
        return True
    else:
        return False

